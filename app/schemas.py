from enum import Enum
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

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    employee_id: Optional[int] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    employee_id: int

    model_config = ConfigDict(from_attributes=True)
