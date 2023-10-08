from Account import *


class Bank():
    
    def __init__(self):

        self.accounts_dict = {}
        self.next_account_number = 0

        self.hours = "9 - 5, Monday - Friday"
        self.web_site = "www.KnewBank.com" 
        self.bank_name = "KnewBank"
        self.location = 'location'
        self.bank_email = 'knewbank@fed.org'
        self.phone = "567-800-9999"
  
    def validate_account_number(self):
        
        account_number = input('Enter your account number')
        try:
                account_number = int(account_number)
        except ValueError:
                raise AbortTransaction('The acount number must be an interger')
        if account_number not in self.accounts_dict:
                raise AbortTransaction('Account number does not exist')
        return account_number

    def get_user_account(self):

        account_number = self.validate_account_number()
        oAccount = self.accounts_dict[account_number]
        self.check_valid_password(oAccount)
        return oAccount


    def open_new_account(self, initial_deposit):
        
        oAccount = Account(self.name, self.balance, self.password)
        
        self.name = str(input("Please enter your full name: " '\n'))
        self.initial_deposit = int(input("Please enter your initial deposit amount: \n"))
        self.password = str(input("Please enter a password: "'\n',
                                        "Passwords must be 6 characters" '\n'))
        if len(self.password) <= 5:
            raise Exception("Password too short")
        
        self.balance = self.balance + initial_deposit
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = oAccount
        self.next_account_number = self.next_account_number + 1
        
        return new_account_number


#=======================#