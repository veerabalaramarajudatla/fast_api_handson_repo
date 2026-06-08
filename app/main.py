from fastapi import FastAPI
from app.routers.employee import router
from app.routers.manager import mrouter
from app.database.connection import engine
from sqlalchemy import text

app = FastAPI()
app.include_router(router)
app.include_router(mrouter)

@app.get("/")
def health_check():

    try:

        with engine.connect() as conn:

            result = conn.execute(
                text("SELECT 'Database Connected'")
            )

            return {
                "status": "UP",
                "database": result.scalar()
            }

    except Exception as e:

        return {
            "status": "DOWN",
            "error": str(e)
        }

@app.get("/{name}")
def name_fun(name):
    return{
        "The name which you have give is :": name
    }