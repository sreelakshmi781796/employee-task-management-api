from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
        
        
from typing import Optional

from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    employee_id: int


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    employee_id: int

    class Config:
        from_attributes = True