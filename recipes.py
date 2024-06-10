import requests
from dotenv import load_dotenv
import os

URL = "https://api.edamam.com/search"

load_dotenv()

PARAMS = {
    "app_id": os.getenv("APP_ID"),
    "app_key": os.getenv("APP_KEY"),
    "from": 0,
    "to": 10,
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
                "source": hit["recipe"]["source"],
                "url": hit["recipe"]["url"],
            }
            for hit in data.get("hits", [])
        ]
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)
