from pydantic import BaseModel, Field
from service.types import ShortCode
from datetime import datetime


class Source(BaseModel):
    origin: str
    short_code: ShortCode
    touch_count: int = 0
    last_update: datetime = Field(default_factory=datetime.now)
