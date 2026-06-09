from fastapi import APIRouter
from app.schemas.employee import Employee
from app.services.employee_service import (get_all_employees,add_employe,get_spicf_emp,del_emp, update_employee, get_team_employee)

router = APIRouter(tags=["Employee"])

@router.post("/employee/add")
def add_employee(employee: Employee):
    return add_employe(employee)

@router.get("/employee/get/all")
def get_all():
    return get_all_employees()

@router.get("/employee/get/{id}")
def get_id(id:int):
    return get_spicf_emp(id)

@router.delete("/employee/drop/{id}")
def drop_employee(id:int):
    return del_emp(id)

@router.put("/employee/update/{id}")
def update_of_employee(id:int, employee: Employee):
    return update_employee(id, employee)

@router.get("/employee/get_team/{team}")
def get_by_team(team:str):
    return get_team_employee(team)