import logging
import time
import random

logging.basicConfig(
    filename = "failure_logs_pra46.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def call_API():
    if False:
       logging.info("Call_API function succsessfully called..")
       return "Succsess"
    raise Exception("API call failed...")

def retry_logic(retry = 3):
    for attempt in range(1,retry+1):
      try:
        result = call_API()
        logging.info("API Called successfully...")
        return result
    
      except Exception as e:
        logging.warning("API call is failed | attempt : %s |Reason : %s",attempt,e)
        time.sleep(attempt)

    logging.error("The API called is failed (Retries failed..)") 
    return None

called = retry_logic()

print(called)