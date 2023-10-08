'''Practice program for modeling a Bank account system - "OOPython" by: Irv Kalb'''
from Bank import *
from Account import *

oBank = Bank()
oAccount = Account

while True:
    
    print("What would you like to do? \n",
          "Press S for Account info. \n",
          "Press B for balance. \n",
          "Press D to make a deposit. \n",
          "Press W for withdrawl. \n",
#          "Press I for Bank info. \n",
          "Press C to create new account. \n",
          "Press Q to quit. \n",

          )
    
    
    answer = input('Please select: ')
    answer = answer.lower()
    answer = answer[0]

    try:

        if answer == 'c':
            print('Create New Account')
            oBank.open_new_account()


        elif answer == 'b':
            print('Get Account Balance')
            oAccount.get_balance()


        elif answer == 'd':
            print('Make a Deposit')
            oAccount.deposit()


        elif answer == 'w':
            print('Make A Withdrawl')
            oAccount.withdraw()


        elif answer == 's':
            print('Show Account Information')
            oAccount.show_account()


        elif answer == 'i':
            print('Show Bank Info')
            oBank.bank_info()


        elif answer == 'q':
            print('Quitting Program...Goodbye')
        break

    
    except AbortTransaction as error:
        print('Transaction has been canceled')

print('Done')


# Account.open_new_account('Eric', 5000, 'wordpass')
# print(Bank.accounts_dict[0]) 