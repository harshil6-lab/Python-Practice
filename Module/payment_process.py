from validation import payment_validation
from loger import loging_configuration
import logging

def payment_withdraw(user_id,amount):
    retry = 3
    
    for attempt in range(1,retry+1):
     try:
      valid,result = payment_validation(amount)
      
      if not valid:
        logging.error("The Validation is Not succeed | user_id : %s | amount : %s",user_id,amount)
        return result
      
      logging.info("Payment is Widrawed | user_id : %s | Amount : %s",user_id,amount)
      return result

     except Exception as e:
       logging.warning("The Payment widtrawing is faied | attempt : %s | user_id : %s | amount : %s | Reason : %s",attempt,user_id,amount,e)

    logging.critical("Payment is permanently failed after %s attempts for user_id : %s of amount : %s",attempt,user_id,amount )
    return None
