from pydantic import BaseModel

class Manager(BaseModel):
    name: str
    designation : str
    team : str
    age : int
    id : int