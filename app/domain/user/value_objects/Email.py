from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core import core_schema


class Email(BaseModel):
    value: EmailStr

    @classmethod
    @field_validator('value')
    def validate_email(cls, v):
        return v.lower()
