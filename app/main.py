from fastapi import FastAPI, Query, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
from tempfile import NamedTemporaryFile
from recipes import fetch_recipes
from prediction import predict_image
import shutil

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello! We are Rechef team!"}


@app.get("/recipes")
def fetch_recipes_endpoint(q: str, _cont: Optional[str] = Query(None)):
    try:
        page, recipes, continuation_token = fetch_recipes(q, _cont)
        return JSONResponse(
            content={
                "page": page,
                "recipes": recipes,
                "continuation_token": continuation_token,
            }
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/prediction")
async def predict_image_endpoint(file: UploadFile = File(...)):
    try:
        with NamedTemporaryFile(delete=False) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_file_path = temp_file.name
        class_name, confidence = predict_image(temp_file_path)
        return JSONResponse(
            content={"class_name": class_name, "confidence": confidence}
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        file.file.close()
