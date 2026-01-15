import os
import logging
from dotenv import load_dotenv
from config_loader import config_loader
import json
import requests
from logger import logging_config
import time

load_dotenv()
config = config_loader()
logging_config()
MAX_RETRIES = config["maximum_retry"]
sleep_time = config["sleep_time"]

ENV = os.getenv("API_URL")
def checkAPI():
    for attempt in range(1,MAX_RETRIES + 1):
        try:
            response = requests.get(ENV,timeout=5)
            
            if response.status_code == 200:
                logging.info("API call is successful on attempt : %s",attempt)
                return response.json()
            else:
                raise Exception("API call failed with status code: %s",format(response.status_code))
        except Exception as e:

          logging.error("Error occurred during API call: %s",str(e))
           #backoff 
          time.sleep(sleep_time)
          sleep_time *=2
          logging.info("Sleeping for %s seconds before retrying",sleep_time)
          logging.info("Retrying API call, attempt %s",attempt)

    logging.critical("Max retries reached. API call is unsuccessful.",)
    return None


result  = checkAPI()
print(result)