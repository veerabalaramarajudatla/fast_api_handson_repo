from fastapi import APIRouter
from app.schemas.employee import Employee
from app.services.employee_service import employees

router = APIRouter()

@router.post("/employee/add")
def add_employee(employee: Employee):
    employees.append(employee)
    return {
        "message": "Employee Added"
    }

@router.get("/employee/getall")
def get_all():
    return employees

@router.delete("/employee/drop/{id}")
def drop_employee(id:int):
    employees.remove(id)
    return {
        "message" : "Employee Droped"
    }