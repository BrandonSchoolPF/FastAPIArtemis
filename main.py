from fastapi import FastAPI
import requests

#Initializing API address and API Key
API_Add = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/'
#API_Host = "X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
headers = {	"X-RapidAPI-Key": "INSERT KEY"}

#Iniitializing Fast App
app = FastAPI()

#Homepage
@app.get("/")
def index():
    req = requests.get(API_Add, headers=headers)
    data = req.json()
    return data


#MilPlane
@app.get("/milplane")
def MilPlane():

    url_mil = "https://adsbexchange-com1.p.rapidapi.com/v2/mil/"

    headers_mil = {
	"X-RapidAPI-Key": "INSERT KEY",
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
        }
    
    req_mil = requests.get(url_mil, headers=headers_mil)

    data_mil = req_mil.json()

    return data_mil

#To Run docker: docker compose up --build
#https://dev.to/rajeshj3/dockerize-fastapi-project-like-a-pro-step-by-step-tutorial-7i8
