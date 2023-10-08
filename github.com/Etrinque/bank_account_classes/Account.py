

class Account():
    
    def __init__(self, name, balance, password):
        self.name = str(name)
        self.balance = int(balance)
        self.password = str(password)

    def deposit(self, deposit_ammount, password):
        if password != self.password:
            print('Sorry. Password Incorrect')
            return None
        if deposit_ammount <= 0:
            print('Cannot deposit negative $')
            return None
        self.balance = self.balance + deposit_ammount
        return self.balance
    
    def withdraw(self, withdrawl_amount, password):
        if password != self.password:
            print('Sorry. Password Incorrect')
            return None
        if withdrawl_amount > self.balance:
            print('Balance insufficient')
            return None
        self.balance = self.balance - withdrawl_amount
        return self.balance
    
    def get_balance(self, password):
        if password != self.password:
            print('Sorry. Password Incorrect')
            return None
        return self.balance
    
    def show_account(self):
        print(f'Acct_Holder: {self.name}')
        print(f'Acct_Bal: {self.balance}')
        print(f'Acc_PW: {self.password}')
        print()

    def open_new_account(self, initial_deposit, password):
        
        oAccount = Account(self.name, self.balance, self.password)
        
        self.name = input("Please enter your full name: " '\n')
        
        initial_deposit = int(input("Please enter your initial deposit amount: \n"))
        self.balance = self.balance + initial_deposit
        
        self.password = input("Please enter a password: "'\n',
                                "Passwords must be 6 characters" '\n')
        if len(self.password) <= 5:
            raise Exception(f"Password too short")
        
        self.accounts_dict[new_account_number] = oAccount

        new_account_number = self.next_account_number
        self.next_account_number = self.next_account_number + 1
        
        return "Account Created, your account id is {new_account_number}"

