#This is designed to hold all of our functions
from fastapi import FastAPI, HTTPException
import requests
from functions import *
import logging
import datetime;

#Logging Function
def configure_logging(): #This sets the logger level
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

logger = configure_logging()

<<<<<<< Updated upstream
def log_endpoint_access(logger, endpoint_name): #This calls logger with endpoint
    #Initiating ct which calls system time
    ct = datetime.datetime.now()

    #ip_address = request.client.host
    #logger.info(f"Source IP: {ip_address}")
=======
#Obtaining the json responses <- get_json_response
def get_json_response(url, headers, endpoint_name):
    url = f"{url}"
 
    # Make an HTTP GET request to the API with the specified headers
    response = requests.get(url, headers=headers)
 
    if response.status_code == 200:
        ct = datetime.datetime.now()

        # Accessing the client's IP address from the request object
        #ip_address = request.client.host

        # Logging the source IP address to the logger
        #logger.info(f" Source IP: {ip_address}")
>>>>>>> Stashed changes

        #Actual Logging info
        logger.info(f" Making API call to: {endpoint_name} ") #Shows that it was successful
        logger.info(f" Accessing {endpoint_name} endpoint Successful") #What endpoint is being accessed
        print(f"Accessed the {endpoint_name} endpoint at", ct) #The time the endpoint is being accessed
        return response.json()
        
    else:
        # Raise an exception with the appropriate status code and error message
        logger.info(f" Making API call to: {endpoint_name} was unsuccessful") #Shows that it was successful
        raise HTTPException(status_code=response.status_code, detail=f"Request failed with status code: {response.status_code}")



    

