from fastapi import FastAPI
from config import RAPIDAPI_KEY, RAPIDAPI_HOST, API_STARTER, IEX_LAT_LON, IEX_API_URL, INTERVAL_SECONDS
#This is where get_json_response comes from
from functions import *
from dotenv import load_dotenv
import os


load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
#Initializing API address and API Key

#####ADS-B######
#Milplane Endpoint and Headers
mil_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/mil/' #Military plane endpoints
IEX_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/' #IEX HQ Endpoint

ads_headers = {	"X-RapidAPI-Key": "25649f62f2msh3808137a2442080p186039jsn6c56c32c82f",	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com" }




#Iniitializing Fast App
app = FastAPI()


# Obtain Refresh Times (In Seconds)
@app.get("/times")
async def refresh_times(request: Request):
    print(f"Accessing the times endpoint at", datetime.datetime.now())
    return {"ADS-B Calls": INTERVAL_SECONDS}
    


#Homepage, this returns IEX HQ
@app.get("/get_data")
async def index(request: Request):
    return get_json_response(IEX_API_URL, ads_headers, "get_data", request)


#MilPlane, This returns Milplane
@app.get("/milplane")
async def MilPlane(request: Request):
    return get_json_response(API_STARTER + "/mil/", ads_headers, "milplane", request)

# This returns aircraft around the selected number of 
# nautical (nm) miles
@app.get("/dist/{int_nm}")
async def dist(int_nm: int, request: Request):
    return get_json_response(API_STARTER + IEX_LAT_LON + f"/dist/{int_nm}", ads_headers, "dist", request)                         

# This returns aircraft based on the inputed icao
@app.get("/icao/{icao}")
async def icao(icao: str, request: Request):
    return get_json_response(API_STARTER + f"/icao/{icao}", ads_headers, "icao", request)

# This returns aircraft based on the inputed hex
@app.get("/hex/{hex}")
async def hex(hex: str, request: Request):
    return get_json_response(API_STARTER + f"/hex/{hex}", ads_headers, "hex", request)

# This returns aircraft based on the inputed squawk code
@app.get("/squawk/{squawk}")
async def squawk(squawk: str, request: Request):
    return get_json_response(API_STARTER + f"/sqk/{squawk}", ads_headers, "squawk", request)

# This returns aircraft based on the inputed squawk code
@app.get("/callsign/{callsign}")
async def callsign(callsign: str, request: Request):
    return get_json_response(API_STARTER + f"/callsign/{callsign}", ads_headers, "callsign", request)