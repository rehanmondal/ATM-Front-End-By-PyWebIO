from pywebio.input import *
from pywebio.output import *
from atm_by_pyweb import ATM

atm =ATM()

def Dashboard_operation():

    dashboard_operation = radio(options=['Withdraw Cash','Balance Enquiry','Pin Change','Other Banking'])


    if dashboard_operation=='Withdraw Cash':
        atm.withdraw_cash()

    elif dashboard_operation=='Balance Enquiry':
        atm.Balance_enquiry()
    
    elif dashboard_operation=='Pin Change':
        atm.Pin_Change()

    elif dashboard_operation=='Other Banking':
        atm.Other_banking()

Dashboard_operation()
