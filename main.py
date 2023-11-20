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

ads_headers = {	"X-RapidAPI-Key": "25649f62f2msh3808137a2442080p186039jsn6c56c32c82",	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com" }




#Iniitializing Fast App
app = FastAPI()


# Obtain Refresh Times (In Seconds)
@app.get("/times")
<<<<<<< Updated upstream
async def refresh_times():
    log_endpoint_access(logger, "times")
=======
async def refresh_times(request: Request):
    print(f"Accessing the times endpoint at", datetime.datetime.now())
>>>>>>> Stashed changes
    return {"ADS-B Calls": INTERVAL_SECONDS}
    


#Homepage, this returns IEX HQ
@app.get("/get_data")
<<<<<<< Updated upstream
async def index():
    log_endpoint_access(logger, "get_data")
    return get_json_response(IEX_API_URL, ads_headers)
=======
async def index(request: Request):
    #log_endpoint_access(logger,request, "get_data")
    return get_json_response(IEX_API_URL, ads_headers, "get_data")
>>>>>>> Stashed changes


#MilPlane, This returns Milplane
@app.get("/milplane")
<<<<<<< Updated upstream
async def MilPlane():
    log_endpoint_access(logger, "milplane")
    return get_json_response(API_STARTER + "/mil/", ads_headers)
=======
async def MilPlane(request: Request):
    #log_endpoint_access(logger,request, "milplane")
    return get_json_response(API_STARTER + "/mil/", ads_headers, "milplane")
>>>>>>> Stashed changes

# This returns aircraft around the selected number of 
# nautical (nm) miles
@app.get("/dist/{int_nm}")
<<<<<<< Updated upstream
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


=======
async def dist(int_nm: int, request: Request):
    #log_endpoint_access(logger,request ,"dist")
    return get_json_response(API_STARTER + IEX_LAT_LON + f"/dist/{int_nm}", ads_headers, "dist")                         

# This returns aircraft based on the inputed icao
@app.get("/icao/{icao}")
async def icao(icao: str, request: Request):
    #log_endpoint_access(logger, request, "icao")
    return get_json_response(API_STARTER + f"/icao/{icao}", ads_headers, "icao")

# This returns aircraft based on the inputed hex
@app.get("/hex/{hex}")
async def hex(hex: str, request: Request):
    #log_endpoint_access(logger,request, "hex")
    return get_json_response(API_STARTER + f"/hex/{hex}", ads_headers, "hex")

# This returns aircraft based on the inputed squawk code
@app.get("/squawk/{squawk}")
async def squawk(squawk: str, request: Request):
    #log_endpoint_access(logger,request, "squawk")
    return get_json_response(API_STARTER + f"/sqk/{squawk}", ads_headers, "squawk")

# This returns aircraft based on the inputed squawk code
@app.get("/callsign/{callsign}")
async def callsign(callsign: str, request: Request):
    #log_endpoint_access(logger,request, "callsign")
    return get_json_response(API_STARTER + f"/callsign/{callsign}", ads_headers, "callsign")
>>>>>>> Stashed changes
