from enum import Enum

from pydantic import BaseModel, StrictInt, StrictStr, Field


class Status(str, Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class Pet(BaseModel):
    id: StrictInt = None
    name: StrictStr
    category: StrictStr = None
    photo_urls: list[StrictStr] = Field(alias="photoUrls")
    tags: list[StrictStr] = None
    status: Status = None


pets: list[Pet] = []
