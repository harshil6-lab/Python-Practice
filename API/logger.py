import logging
from config_loader import config_loader

config = config_loader()
FILE = config["log_file"]

def logging_config():
 logging.basicConfig(

    filename = FILE,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    force = True
  )
