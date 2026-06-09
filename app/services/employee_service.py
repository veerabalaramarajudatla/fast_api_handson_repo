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

def update_employee(id: int, employee: Employee):
    update_fields = []
    params = {"id": id}
    
    if employee.name is not None:
        update_fields.append("name = :name")
        params["name"] = employee.name

    if employee.age is not None:
        update_fields.append("age = :age")
        params["age"] = employee.age

    if employee.designation is not None:
        update_fields.append("designation = :designation")
        params["designation"] = employee.designation

    if employee.team is not None:
        update_fields.append("team = :team")
        params["team"] = employee.team

    if not update_fields:
        return {"message": "No fields provided"}

    query = text(f"""
        UPDATE employee
        SET {", ".join(update_fields)}
        WHERE id = :id
    """)

    with engine.begin() as conn:

        result = conn.execute(
            query,
            params
        )

    return {
        "rows_updated": result.rowcount
    }

def get_team_employee(team: str):
    query = text("""
        select * from employee where team = :team
    """)
    with engine.begin() as conn:
        result = conn.execute(query,{"team":team})
        rows = result.mappings().all()
    return rows