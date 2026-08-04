from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr