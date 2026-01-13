import logging

def loging_configuration():
  logging.basicConfig(
    filename = "logging_for_payment.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
    )