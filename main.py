from fastapi import FastAPI
from config import RAPIDAPI_KEY, RAPIDAPI_HOST, API_STARTER, IEX_LAT_LON, IEX_API_URL, INTERVAL_SECONDS
import requests
#This is where get_json_response comes from
from functions import *
import datetime

#Initializing API address and API Key

#####ADS-B######
#Milplane Endpoint and Headers
mil_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/mil/' #Military plane endpoints
IEX_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/' #IEX HQ Endpoint

ads_headers = {	"X-RapidAPI-Key": RAPIDAPI_KEY,	"X-RapidAPI-Host": RAPIDAPI_HOST }


#Iniitializing Fast App
app = FastAPI()

# Obtain Refresh Times (In Seconds)
@app.get("/times")
async def refresh_times():
    log_endpoint_access(logger, "times")
    return {"ADS-B Calls": INTERVAL_SECONDS}
    


#Homepage, this returns IEX HQ
@app.get("/get_data")
async def index():
    log_endpoint_access(logger, "get_data")
    return get_json_response(IEX_API_URL, ads_headers)


#MilPlane, This returns Milplane
@app.get("/milplane")
async def MilPlane():
    log_endpoint_access(logger, "milplane")
    return get_json_response(API_STARTER + "/mil/", ads_headers)

# This returns aircraft around the selected number of 
# nautical (nm) miles
@app.get("/dist/{int_nm}")
async def dist(int_nm: int):
    log_endpoint_access(logger, "dist")
    return get_json_response(API_STARTER + IEX_LAT_LON + f"/dist/{int_nm}", 
                            ads_headers)                         

# This returns aircraft based on the inputed icao
@app.get("/icao/{icao}")
async def icao(icao: str):
    log_endpoint_access(logger, "icao")
    return get_json_response(API_STARTER + f"/icao/{icao}", ads_headers)

# This returns aircraft based on the inputed hex
@app.get("/hex/{hex}")
async def hex(hex: str):
    log_endpoint_access(logger, "hex")
    return get_json_response(API_STARTER + f"/hex/{hex}", ads_headers)

# This returns aircraft based on the inputed squawk code
@app.get("/squawk/{squawk}")
async def squawk(squawk: str):
    log_endpoint_access(logger, "squawk")
    return get_json_response(API_STARTER + f"/sqk/{squawk}", 
                                ads_headers)

# This returns aircraft based on the inputed squawk code
@app.get("/callsign/{callsign}")
async def callsign(callsign: str):
    log_endpoint_access(logger, "callsign")
    return get_json_response(API_STARTER + f"/callsign/{callsign}", 
                                ads_headers)


