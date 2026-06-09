from fastapi import APIRouter
from app.schemas.manager import Manager
from app.services.manager_service import (add_manager, get_manager_list, get_manager, del_manager, update_manager, team_of_manager)

mrouter = APIRouter(prefix="/manager",tags=["Manager"])

@mrouter.post("/manager/add")
def manager_add(employeemanager : Manager):
    return add_manager(employeemanager)

@mrouter.get("/manager/get/all")
def manager_all():
    return get_manager_list()

@mrouter.get("/manager/get/{id}")
def manager_id(id:int):    
    return get_manager(id)

@mrouter.delete("/manager/delete/{id}")
def manger_del(id:int):
    return del_manager(id)

@mrouter.put("/manager/update/{id}")
def update_of_manager(id:int, employeemanager: Manager):
    return update_manager(id, employeemanager)

@mrouter.get("/manager/team/{id}")
def team_of_the_manager(id:int):
    return team_of_manager(id)