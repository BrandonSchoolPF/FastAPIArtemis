#This is designed to hold all of our functions
from fastapi import FastAPI
import requests
from functions import *



#Obtaining the json responses <- get_json_response
def get_json_response(url, headers):
    url = f"{url}" #Endpoint should be above 'Mil', 'IEX'...
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle the case where the API request failed
        print(f"Request failed with status code: {response.status_code}")