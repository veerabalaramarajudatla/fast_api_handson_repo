from sqlalchemy import text
from app.database.connection import engine
from app.schemas.manager import Manager

def add_manager(employeemanager: Manager):
    query = text("""
        INSERT INTO manager (name, designation, team, age)
        VALUES(:name, :designation, :team, :age)
    """)
    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "name": employeemanager.name,
                "designation" :employeemanager.designation,
                "team" : employeemanager.team,
                "age": employeemanager.age
            }
        )
    return {"message": "Manager Employee Added"}

def get_manager_list():
    query = text("""
        SELECT * FROM manager
    """)
    with engine.begin() as conn:
        result = conn.execute(query)
        rows = result.mappings().all()
    return rows

def get_manager(id:int):
    query = text("""
        selct * from manager where id = :id
    """)
    with engine.begin() as conn:
        result = conn.execute(query,{"id": id})
        rows = result.mappings().first()
    return rows

def del_manager(id:int):
    query = text("""
        DELETE FROM manger WHERE id = :id            
    """)
    with engine.begin() as conn:
        result = conn.execute(query,{"id": id})
    
    return {
        "message": "Employee Manager Deleted",
        "rows_affected": result.rowcount
    }