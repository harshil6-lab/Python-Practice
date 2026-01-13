def payment_validation(amount):
    balance = 100
    if amount <= 0:
      return False,"Error : Invalid amount , Please Enter valid Amount (>0)"
    if balance < amount:
      raise Exception("insufficient Amount")
    return True,"Payment widrawed Succsessfully"