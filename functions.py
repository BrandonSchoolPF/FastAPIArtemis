#This is designed to hold all of our functions
from fastapi import FastAPI, HTTPException
import requests
from functions import *

# Method for making API requests and handling responses
def get_json_response(url, headers):
    url = f"{url}"

    # Make an HTTP GET request to the API with the specified headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            # Return a JSON response to view in browser
            return response.json()
        except ValueError:
            raise HTTPException(status_code=500, detail="Response is not valid JSON.")
    else:
        # Raise an exception with the appropriate status code and error message
        raise HTTPException(status_code=response.status_code, detail=f"Request failed with status code: {response.status_code}")

