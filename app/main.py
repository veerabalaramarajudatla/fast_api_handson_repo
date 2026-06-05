from fastapi import FastAPI
from app.routers.employee import router
from app.routers.manager import mrouter

app = FastAPI()
app.include_router(router)
app.include_router(mrouter)

@app.get("/")
def health_check():
    return {
        "status": "UP"
    }

@app.get("/{name}")
def name_fun(name):
    return{
        "The name which you have give is :": name
    }