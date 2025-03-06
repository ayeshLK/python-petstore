from fastapi import APIRouter, HTTPException
from model.pet import Status, Pet, pets
from typing import List

router = APIRouter()


@router.post("/pets", response_model=int)
async def add_new_pet(pet: Pet):
    """
    Add a new pet to the system.

    - **Request Body:** Pet details (name, category, photo URLs, tags)
    - **Response:** Returns the newly assigned pet ID.
    - **Default Status:** The pet is marked as `available` upon creation.
    """
    pet_id: int = len(pets) + 1
    pet.id = pet_id
    pet.status = Status.available
    pets.append(pet)
    return pet_id


@router.get("/pets/findByStatus", response_model=List[Pet])
async def find_pets_by_status(status: Status):
    """
    Find pets by status.

    - **Query Parameter:** `status` (available, pending, or sold)
    - **Response:** Returns a list of pets matching the given status.
    """
    return [pet for pet in pets if pet.status == status]


@router.get("/pets/findByTags", response_model=List[Pet])
async def find_pets_by_tags(tags: List[str]):
    """
    Find pets by tags.

    - **Query Parameter:** `tags` (List of strings)
    - **Response:** Returns a list of pets containing any of the specified tags.
    """
    return [
        pet for pet in pets
        if pet.tags and any(tag in pet.tags for tag in tags)
    ]


@router.get("/pets/{pet_id}", response_model=Pet)
async def find_pet_by_id(pet_id: int):
    """
    Find a pet by its ID.

    - **Path Parameter:** `pet_id` (integer)
    - **Response:** Returns the pet details if found.
    - **Error Handling:** Returns `404 Not Found` if the pet does not exist.
    """
    pet = next((pet for pet in pets if pet.id == pet_id), None)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet


@router.delete("/pets/{pet_id}", response_model=str)
async def delete_pet_by_id(pet_id: int):
    """
    Delete a pet by its ID.

    - **Path Parameter:** `pet_id` (integer)
    - **Response:** Confirms deletion of the pet.
    - **Error Handling:** If the pet ID is not found, no action is taken.
    """
    global pets
    pets = [pet for pet in pets if pet.id != pet_id]
    return f"Pet with ID {pet_id} has been deleted."
