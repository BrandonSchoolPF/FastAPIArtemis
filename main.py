# Import necessary libraries
import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

#Iniitializing Fast App
app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Define constants and set up headers for API requests
PORT = 8000
API_KEY = os.getenv('API_KEY')

##ADS-B##
mil_ads = "https://adsbexchange-com1.p.rapidapi.com/v2/mil"
IEX_ads = "https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/"
ads_headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": 'adsbexchange-com1.p.rapidapi.com'
}

# Method for making API requests and handling responses
def create_api_reqest(url, headers):
    url = f"{url}"
    
    # Print the API request URL for debugging purposes1
    print("Making API call to: ", url)

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

# Define a FastAPI route to handle requests to "/tagged-aircrafts"
@app.get("/tagged-aircrafts")
async def get_tagged_aircraft_data():
    return create_api_reqest(mil_ads, ads_headers)

# Define a FastAPI route to handle requests to "/overhead-iex"
@app.get("/overhead-iex")
async def get_overhead_iex_data():
    return create_api_reqest(IEX_ads, ads_headers)