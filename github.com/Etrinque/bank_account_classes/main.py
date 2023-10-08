'''Practice program for modeling a Bank account system - "OOPython" by: Irv Kalb'''
from Account import *


class Bank():
    
    def __init__(self):
        
        self.hours = "9 - 5, Monday - Friday"
        self.web_site = "www.KnewBank.com" 
        self.bank_name = "KnewBank"
        self.location = 'location'
        self.bank_email = 'knewbank@fed.org'
        self.phone = "567-800-9999"

        self.accounts_dict = {}
        self.next_account_number = 0
    
while True:
    
    print("What would you like to do? \n",
          "Press S for Account info. \n",
          "Press B for balance. \n"
          "Press D to make a deposit. \n",
          "Press W for withdrawl. \n",
#          "Press I for Bank info. \n",
          "Press C to create new account. \n",
          "Press Q to quit. \n",

          )
    
    input('Please select: ')
    answer = str(input)
    answer = answer[0]

    try:
        if answer.lower() == 'c':
            Bank.open_new_account()
        elif answer.lower() == 'b':
            Account.get_balance()
        elif answer.lower() == 'd':
            Account.withdraw()
        elif answer.lower() == 'w':
            Account.deposit()
        elif answer.lower() == 's':
            Account.show_account()
#        elif answer.lower == 'i':
#            Bank.bank_info()
        elif answer.lower() == 'q':
            break
        break 
    except AbortTransaction as error:
        print('Transaction has been canceled')



def AbortTransaction():
    pass




"""TEST"""
Account.open_new_account('Eric', 4000, 'string')