from Account import *
from main import *

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