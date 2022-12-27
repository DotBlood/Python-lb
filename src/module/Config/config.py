import os
from dotenv import load_dotenv, find_dotenv


def getApiKey():
    load_dotenv(find_dotenv())
    APIKEY = os.environ.get("API_KEY")
    return APIKEY