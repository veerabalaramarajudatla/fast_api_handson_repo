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

def update_manager(id: int, employeemanager: Manager):
    update_fields = []
    params = {"id": id}
    
    if employeemanager.name is not None:
        update_fields.append("name = :name")
        params["name"] = employeemanager.name

    if employeemanager.age is not None:
        update_fields.append("age = :age")
        params["age"] = employeemanager.age

    if employeemanager.designation is not None:
        update_fields.append("designation = :designation")
        params["designation"] = employeemanager.designation

    if employeemanager.team is not None:
        update_fields.append("team = :team")
        params["team"] = employeemanager.team

    if not update_fields:
        return {"message": "No fields provided"}

    query = text(f"""
        UPDATE manager
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

def team_of_manager(id: int):
    query = text("""
        select m.id AS manager_id, m.name AS manager_name,
            m.team, e.id AS employee_id, e.name AS employee_name,
            e.designation from manager m left join 
            employee e on m.team = e.team where m.id = :id
    """)
    with engine.begin() as conn:
        result=conn.execute(query,{"id": id})
        rows = result.mappings().all()
    return rows

def team():
    query = text("""
        select m.id as manager_id, m.name as manager_name, e.id as employee_id, e.name as employee_name from manager m left join employee e on m.team = e.team
    """)
    with engine.begin() as conn:
        result = conn.execute(query)
        rows = result.mappings().all()
    return rows