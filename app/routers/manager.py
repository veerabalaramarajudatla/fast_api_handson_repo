from fastapi import APIRouter
from app.schemas.manager import Manager
from app.services.manager_service import (add_manager, get_manager_list, get_manager, del_manager)

mrouter = APIRouter()

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