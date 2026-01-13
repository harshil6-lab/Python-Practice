import logging
from config_load import config_loader

file_loading = config_loader()
FILE= file_loading["log_file"]

def loging_configuration():
  logging.basicConfig( 
    filename =  FILE,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    force = True
    )