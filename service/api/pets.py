from fastapi import APIRouter, HTTPException
from model.pet import Status, Pet, pets

router = APIRouter()


@router.post("/pets")
async def add_new_pet(pet: Pet):
    pet_id: int = len(pets) + 1
    pet.id = pet_id
    pet.status = Status.available
    pets.append(pet)
    return pet_id


@router.get("/pets/findByStatus")
async def find_pets_by_status(status: Status):
    return [pet for pet in pets if pet.status == status]


@router.get("/pets/findByTags")
async def find_pets_by_tags(tags: list[str]):
    return [
        pet for pet in pets
        if pet.tags and any(tag in pet.tags for tag in tags)
    ]


@router.get("/pets/{pet_id}")
async def find_pet_by_id(pet_id: int):
    pet = next((pet for pet in pets if pet.id == pet_id), None)
    if pet is None:
        return HTTPException(status_code=404, detail="Pet not found")
    return pet


@router.delete("/pets/{pet_id}")
async def delete_pet_by_id(pet_id: int):
    global pets
    pets = [pet for pet in pets if pet.id != pet_id]
