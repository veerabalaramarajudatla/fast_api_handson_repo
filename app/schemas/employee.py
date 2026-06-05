from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    designation : str
    age : int
    id : int