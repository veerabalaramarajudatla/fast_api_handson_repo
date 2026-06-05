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

@router.get("/employee/get/all")
def get_all():
    return employees

@router.get("/employee/get/{id}")
def get_id(id:int):
    for employee in employees:
        if employee.id == id:
            return employee
    
    return {
        "message" : "Employee Not Found"
    }


@router.delete("/employee/drop/{id}")
def drop_employee(id:int):
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
        return {
            "message" : "Employee Droped"
        }
    
    return {
        "message" : "Employee not present"
    }