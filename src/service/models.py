import secrets
from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel
from pydantic import Field
from service.types import ShortCode


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


def make_short_code() -> ShortCode:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(secrets.choice(chars) for _ in range(5))



class Source(BaseModel):
    origin: str

    touch_count: int = 0
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    # TODO: make unique
    short_code: ShortCode = Field(default_factory=make_short_code)
    last_update: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            ObjectId: lambda v: str(v),
            PyObjectId: lambda v: str(v),
            datetime: lambda dt: dt.isoformat(),
        }
