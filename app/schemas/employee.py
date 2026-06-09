from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    designation: Optional[str] = None
    team: Optional[str] = None