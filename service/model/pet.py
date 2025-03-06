from enum import Enum
from pydantic import BaseModel, StrictInt, StrictStr, Field
from typing import List, Optional


class Status(str, Enum):
    """
    Enum representing the status of a pet.
    """
    available = "available"  # Pet is available for adoption/purchase
    pending = "pending"  # Adoption/purchase is in progress
    sold = "sold"  # Pet has been adopted/purchased


class Pet(BaseModel):
    """
    Represents a pet in the system.
    """
    id: Optional[StrictInt] = Field(
        None, description="Unique identifier for the pet"
    )
    name: StrictStr = Field(
        ..., description="Name of the pet"
    )
    category: Optional[StrictStr] = Field(
        None, description="Category of the pet (e.g., dog, cat, bird)"
    )
    photo_urls: List[StrictStr] = Field(
        ..., alias="photoUrls", description="List of photo URLs for the pet"
    )
    tags: Optional[List[StrictStr]] = Field(
        None, description="Tags describing the pet (e.g., friendly, small)"
    )
    status: Optional[Status] = Field(
        None, description="Current status of the pet"
    )


pets: list[Pet] = []
