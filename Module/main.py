#Documentation for pra48.py
#learning....
#  what is modeule ? - > Module is a file that with a clear responsibility.
#  what is package ? - > package is a collection of modules.

from payment_process import payment_withdraw
from loger import loging_configuration
loging_configuration()
result1 = payment_withdraw(101,100)
print(result1)
result2 = payment_withdraw(102,100.55)
print(result2)
