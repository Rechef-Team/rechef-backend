from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from recipes import fetch_recipes

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello! We are Rechef team!"}


@app.get("/get_recipes")
def get_recipes(q: str, _cont: Optional[str] = Query(None)):
    try:
        page, recipes, continuation_token = fetch_recipes(q, _cont)
        return {"page": page, "recipes": recipes, "_cont": continuation_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
