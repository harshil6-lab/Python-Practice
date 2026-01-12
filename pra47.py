import logging

logging.basicConfig(
    filename = "logging_of_pra47",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#function as reusable.
def payment_validation(amount,balance):
    if amount <= 0:
      return False,"Error : Invalid amount , Please Enter valid Amount (>0)"
    if balance < amount:
      raise Exception("insufficient Amount")
    return True,"Payment widrawed Succsessfully"
  
def payment_widraw(user_id,amount):
    retry = 3
    
    for attempt in range(1,retry+1):
     try:
      valid,result = payment_validation(amount,100)
      
      if not valid:
        logging.error("The Validation is Not succeed | user_id : %s | amount : %s",user_id,amount)
        return result
      
      logging.info("Payment is Widrawed | user_id : %s | Amount : %s",user_id,amount)
      return result

     except Exception as e:
       logging.warning("The Payment widtrawing is faied | attempt : %s | user_id : %s | amount : %s | Reason : %s",attempt,user_id,amount,e)

    logging.critical("Payment is permanently failed after %s attempts for user_id : %s of amount : %s",attempt,user_id,amount )
    return None


print(payment_widraw(102,200))