from fastapi import APIRouter
from app.schemas.manager import Manager
from app.services.manager_service import manager

mrouter = APIRouter()

@mrouter.post("/manager/add")
def manager_add(employeemanager : Manager):
    manager.append(employeemanager)
    return {
        "Message" : "New Manager has been added"
    }

@mrouter.get("/manager/get/all")
def manager_all():
    return manager

@mrouter.get("/manager/get/{id}")
def manager_id(id:int):
    for m in manager:
        if m.id == id:
            return m
    
    return {
        "Message" : "Manager not found"
    }

@mrouter.delete("/manager/delete/{id}")
def manger_del(id:int):
    for m in manager:
        if manager.id == id:
            manager.remove(m)
    return {
        "Message" : "Manager Removed"
    }