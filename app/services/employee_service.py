from sqlalchemy import text
from app.database.connection import engine
from app.schemas.employee import Employee

def add_employe(employee: Employee):
    query = text("""
        INSERT INTO employee(name, age, designation, team)
        VALUES(:name, :age, :designation, :team)
    """)
    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "name": employee.name,
                "age": employee.age,
                "designation" :employee.designation,
                "team" : employee.team
            }
        )
    return {"message": "Employee Added"}

def get_all_employees():
    query = text("""
        SELECT *
        FROM employee
    """)
    with engine.connect() as conn:
        result = conn.execute(query)
        rows = result.mappings().all()
    return rows

def get_spicf_emp(id:int):
    query = text("""
        Select * from employee where id = :id
    """)
    with engine.connect() as conn:
        result = conn.execute(query,{"id": id})
        rows = result.mappings().first()
    return rows

def del_emp(id:int):
    query = text("""
        DELETE FROM employee WHERE id = :id            
    """)
    with engine.begin() as conn:
        result = conn.execute(query,{"id": id})
    
    return {
        "message": "Employee Deleted",
        "rows_affected": result.rowcount
    }