from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate
from app.database.connection import get_db

from app.services.client_service import (create_client,get_all_clients,get_client_by_id)

router = APIRouter(tags=["Client"])