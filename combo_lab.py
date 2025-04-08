import random

class BankAccount:
    def __init__(self, owner, balance, account_type, interest_rate):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.account_num = random.randint(1000000, 1999999)

    def print_details(self):
        print("Owner:", self.owner)
        print("Account Number:", self.account_num)
        print("Account Type:", self.account_type)
        print("Interest Rate:", self.interest_rate)
        print("Current Balance:", self.balance)
        print()

    def get_balance(self):
        print("Current balance: ", self.balance)

    def withdraw(self, amount):
        try:
            if (self.balance - amount < 0):
                raise Exception("Balance too low, cannot withdraw")
            else:
                self.balance -= amount
        except Exception as e:
            print("Error:", e)

            


ba1 = BankAccount("Paul", 50000, "Checking", 1.25)
ba2 = BankAccount("Paul", 500000, "Savings", 2.50)

bank_accounts = [ba1, ba2]

for account in bank_accounts:
    account.print_details()

ba1.withdraw(2000)
ba1.get_balance()

ba1.withdraw(2000000)
ba1.get_balance()

ba1.withdraw("five million dollars")
ba1.get_balance()