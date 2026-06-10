from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.project import ProjectCreate
from app.services.project_service import (create_project,get_all_projects,get_project_by_id,get_projects_by_client)

prouter = APIRouter(tags=["Project"])

@prouter.post("/project/create")
def add_project(project: ProjectCreate,db: Session = Depends(get_db)):
    return create_project(db,project)

@prouter.get("/project/all")
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)

@prouter.get("/project/{project_id}")
def get_project(project_id: str,db: Session = Depends(get_db)):
    return get_project_by_id(db,project_id)

@prouter.get("/client/{client_id}")
def get_client_projects(client_id: str,db: Session = Depends(get_db)):
    return get_projects_by_client(db,client_id)