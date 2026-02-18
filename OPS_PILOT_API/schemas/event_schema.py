from pydantic import BaseModel, field_validator
from typing import Optional


class EventCreateSchema(BaseModel):
    title: str
    raw_logs: str
    description: Optional[str] = None
    status_id: Optional[int] = None
    priority_id: Optional[int] = None

    @field_validator("title", "raw_logs", mode="before")
    @classmethod
    def strip_and_reject_blank(cls, v):
        if isinstance(v, str):
            v = v.strip()
        if not v:
            raise ValueError("Field cannot be blank or whitespace")
        return v
