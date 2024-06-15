import requests
import os
from typing import Optional
from urllib.parse import urlparse, parse_qs

API_URL = "https://api.edamam.com/api/recipes/v2"
PARAMS = {
    "type": "public",
    "app_id": os.getenv("APP_ID"),
    "app_key": os.getenv("APP_KEY"),
}


def fetch_recipes(query: str, continuation_token: Optional[str] = None):
    try:
        params = {**PARAMS, "q": query}
        if continuation_token:
            params["_cont"] = continuation_token

        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        page = {"from": data.get("from", 0), "to": data.get("to", 0)}

        recipes = [
            {
                "label": hit["recipe"]["label"],
                "image": hit["recipe"]["image"],
                "ingredients": hit["recipe"]["ingredientLines"],
                "url": hit["recipe"]["url"],
            }
            for hit in data.get("hits", [])
        ]

        next_page_url = data.get("_links", {}).get("next", {}).get("href")
        continuation_token = (
            parse_qs(urlparse(next_page_url).query).get("_cont", [None])[0]
            if next_page_url
            else None
        )

        return page, recipes, continuation_token

    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        raise
    except requests.RequestException as e:
        print(f"Request error occurred: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
