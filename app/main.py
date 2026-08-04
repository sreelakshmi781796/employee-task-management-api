from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate


app = FastAPI(
    title="Employee Task Management API",
    version="0.1.0",
)


@app.get("/")
def root() -> dict:
    return {"message": "Employee Task Management API"}


@app.get("/health")
def health_check() -> dict:
    return {"status": "healthy"}


@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
) -> Employee:
    existing_employee = db.scalar(
        select(Employee).where(Employee.email == str(employee.email))
    )

    if existing_employee is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        )

    new_employee = Employee(
        name=employee.name,
        email=str(employee.email),
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@app.get(
    "/employees",
    response_model=list[EmployeeResponse],
)
def get_employees(
    db: Session = Depends(get_db),
) -> list[Employee]:
    employees = db.scalars(select(Employee)).all()
    return list(employees)


@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
) -> Employee:
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return employee


@app.patch(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
)
def update_employee(
    employee_id: int,
    employee_update: EmployeeUpdate,
    db: Session = Depends(get_db),
) -> Employee:
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    update_data = employee_update.model_dump(exclude_unset=True)

    # Convert EmailStr into a normal string before saving.
    if "email" in update_data:
        new_email = str(update_data["email"])

        employee_with_email = db.scalar(
            select(Employee).where(
                Employee.email == new_email,
                Employee.id != employee_id,
            )
        )

        if employee_with_email is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An employee with this email already exists",
            )

        update_data["email"] = new_email

    for field, value in update_data.items():
        setattr(employee, field, value)

    db.commit()
    db.refresh(employee)
    
@app.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    db.delete(employee)
    db.commit()

    return None

    return employee