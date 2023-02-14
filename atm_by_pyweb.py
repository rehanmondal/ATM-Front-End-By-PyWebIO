from pywebio.input import *
from pywebio.output import *
from datetime import datetime
now=datetime.now()

# PIN CHANE USING MAX-MIN = 4 DIGIT LIMIT SET REQUIRED
Dict_atm={1234:2000,4567:2500,7892:2300}  # Can add a large Dictionary, Also Execute Perfectly

class ATM:
    def withdraw_cash(self):
        user_pin=int(input("Please Enter your Pin - ", type=NUMBER))
        # amt=int(input("Enter Amount : "))
        if user_pin in Dict_atm.keys():
            var= Dict_atm.get(user_pin)
            amt=int(input("Enter Amount : ",type=NUMBER))
            bal=var-amt     
            Dict_atm['user_pin']=bal
            style(put_text("Last Transaction Completed ! \nAvailable Balance : ",Dict_atm['user_pin']),'color:blue')
        else:
            style(put_text("You have entered a Wrong Pin"),'color:red')
            # Dashboard_operation()

    def Balance_enquiry(self):
        user_pin=int(input("Please Enter your Pin to get Mini Satement- ", type=NUMBER))
        put_text("Available Balance : ",Dict_atm.get(user_pin,"Not showing, You have entered a Wrong Pin"))

    def Pin_Change(self):
        put_text("Front End Coming Soon ! Backend Present In my ATM Terminal Project Repository")

    def Other_banking(self):
        put_text("Front End Coming Soon ! Backend Present In my ATM Terminal Project Repository")


