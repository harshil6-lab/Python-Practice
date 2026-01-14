#Documentation for pra48.py
#learning....
#  what is modeule ? - > Module is a file that with a clear responsibility.
#  what is package ? - > package is a collection of modules.
#Environment variables using pyython-dotenv package.
# In this example we will create a .env file to store environment variables and load them using python-dotenv package.
# We will then use these environment variables in our main.py file to control the behavior of our application based on the environment (development, production, etc.).
# First, we need to install the python-dotenv package if we haven't already.
# pip install python-dotenv
# Next, we create a .env file in the root directory of our project and add some environment variables to it.
# .env file content:
# ENV = "development"
# Now, we will create a main.py file that loads these environment variables and uses them to control the behavior of our application.

import logging
from dotenv import load_dotenv
import os
from payment_process import payment_withdraw
from loger import loging_configuration
load_dotenv()
loging_configuration()

env = os.getenv("ENV")
try : 
   if env !="development":
      logging.error("Environment is not set to Development , Current Environment : %s",env)
      raise SystemExit("Environment is not set to Development , Exiting the Application !")
   else : 
      print("Environment is set to Developement")
except Exception as e :
   logging.error("Environment Error : %s",e)
   print("Environment is not set to Developement . Logging the Error !")

result1 = payment_withdraw(101,100)
print(result1)
result2 = payment_withdraw(102,100.55)
print(result2)


