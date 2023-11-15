import configparser
config = configparser.ConfigParser()
config.read('config.ini')

RAPIDAPI_KEY = config.get('API', 'RAPIDAPI_KEY')
RAPIDAPI_HOST = config.get('API', 'RAPIDAPI_HOST')
IEX_API_URL = config.get('API', 'IEX_API_URL')
API_STARTER = config.get('API', 'API_STARTER')
IEX_LAT_LON = config.get('API', 'IEX_LAT_LON')
PORT = config.getint('API', 'PORT')
INTERVAL_SECONDS = config.getint('SCHEDULER', 'INTERVAL_SECONDS')