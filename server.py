from fastapi import FastAPI
from recipes import get_recipes
import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello! We are Rechef team!"}


@app.get("/get_recipes")
def get_recipes_endpoint(query: str):
    return get_recipes(query)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
