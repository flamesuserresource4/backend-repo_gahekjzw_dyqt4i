from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime


class DemoRequest(BaseModel):
    name: Optional[str] = Field(None, example="Alex Doe")
    email: Optional[EmailStr] = Field(None, example="alex@example.com")
    message: Optional[str] = Field(None, example="We'd like a walkthrough of the platform.")


class DemoResponse(BaseModel):
    status: str
    received_at: datetime

