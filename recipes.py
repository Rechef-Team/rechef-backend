import requests
from dotenv import load_dotenv
import os

URL = "https://api.edamam.com/api/recipes/v2"

load_dotenv()

PARAMS = {
    "type": "public",
    "q": None,
    "app_id": os.getenv("APP_ID"),
    "app_key": os.getenv("APP_KEY"),
    "from": 0,
    "to": 10,
    "imageSize": "REGULAR",
    "Accept-Encoding": "gzip",
}


def get_recipes(query):
    try:
        response = requests.get(URL, params={**PARAMS, "q": query})
        response.raise_for_status()
        data = response.json()
        return [
            {
                "label": hit["recipe"]["label"],
                "image": hit["recipe"]["image"],
                "ingredients": hit["recipe"]["ingredientLines"],
                "url": hit["recipe"]["url"],
            }
            for hit in data.get("hits", [])
        ]
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)
