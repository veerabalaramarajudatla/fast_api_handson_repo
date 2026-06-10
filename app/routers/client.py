from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate
from app.database.connection import get_db

from app.services.client_service import (create_client,get_all_clients,get_client_by_id)

router = APIRouter(tags=["Client"])

@router.post("/client/create")
def add_client(client: ClientCreate,db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/client/all")
def get_clients(db: Session = Depends(get_db)):
    return get_all_clients(db)

@router.get("/client/{client_id}")
def get_client(client_id: str,db: Session = Depends(get_db)):
    return get_client_by_id(db,client_id)