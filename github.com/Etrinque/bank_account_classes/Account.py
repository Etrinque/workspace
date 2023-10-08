
class AbortTransaction(Exception):
    pass

class Account():
    
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validate_amount(balance)
        self.password = password

    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def check_valid_password(self, password):
        if password != self.password:
            raise AbortTransaction('Password invalid')

    def deposit(self, deposit_ammount):
        deposit_ammount = self.validate_amount(deposit_ammount)
        self.balance = self.balance + deposit_ammount
        return self.balance

    def get_balance(self):
        return self.balance
    
    def withdraw(self, withdrawl_amount):
        withdrawl_amount = self.validate_amount(withdrawl_amount)
        if withdrawl_amount > self.balance:
            raise AbortTransaction('Balance insufficient')
        self.balance = self.balance - withdrawl_amount
        return self.balance
    
    def show_account(self):
        print(f'Acct_Holder: {self.name}')
        print(f'Acct_Bal: {self.balance}')
        print(f'Acc_PW: {self.password}')
        print()

