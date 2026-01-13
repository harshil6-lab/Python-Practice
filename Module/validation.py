from config_load import config_loader
file_loading = config_loader()
balance = file_loading["balance"]

def payment_validation(amount):

    if amount <= 0:
      return False,"Error : Invalid amount , Please Enter valid Amount (>0)"
    if balance < amount:
      raise Exception("insufficient Amount")
    return True,"Payment widrawed Succsessfully"