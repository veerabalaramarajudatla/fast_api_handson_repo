from fastapi import FastAPI
from app.routers.employee import router

app = FastAPI()
app.include_router(router)

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