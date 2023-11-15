from fastapi import FastAPI
import requests
#This is where get_json_response comes from
from functions import *

#Initializing API address and API Key

#####ADS-B######
#Milplane Endpoint and Headers
mil_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/mil/' #Military plane endpoints
IEX_ads = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/' #IEX HQ Endpoint
ads_headers = {	"X-RapidAPI-Key": "Insert Key",	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com" }
#####ADS-B######


#Iniitializing Fast App
app = FastAPI()

#Homepage, this returns IEX HQ
@app.get("/")
async def index():
    return get_json_response(IEX_ads, ads_headers)

#MilPlane, This returns Milplane
@app.get("/milplane")
async def MilPlane():
    return get_json_response(mil_ads, ads_headers)
