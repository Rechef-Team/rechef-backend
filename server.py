from fastapi import FastAPI
from recipes import get_recipes

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello! We are Rechef team!"}


@app.get("/get_recipes")
def get_recipes_endpoint(query: str):
    return get_recipes(query)
