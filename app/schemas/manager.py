from pydantic import BaseModel
from typing import Optional

class Manager(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    team: Optional[str] = None
    age: Optional[int] = None 