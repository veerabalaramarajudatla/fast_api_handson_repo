from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello this is a fast API Application"}

@app.get("/{name}")
def returnstring(name):
    return {"The String you have passed is" : name}