from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


# Employee schemas

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


# Task schemas

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    employee_id: int


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    employee_id: Optional[int] = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    status: str
    employee_id: int