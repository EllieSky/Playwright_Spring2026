from datetime import datetime
class BankAccount(object):

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("amount must be a positive number")
            return
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            # print("insufficient funds")
            raise ValueError('Insufficient funds')
        elif amount < 0:
            print("amount must be a positive number")
            return
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account for {self.owner} has current balance of ${self.balance}'



class BankUser:
    def __init__(self, first, last, id):
        self.account_number = datetime.now().timestamp()
        self.account = BankAccount(f"{first} {last}")
        self.accounts = {
            'checking': {self.account_number : self.account},
            'savings': None
        }
        self.id = id

    def wire(self, to_account: BankAccount, amount):
        try:
            self.account.withdraw(amount)
        except ValueError as e:
            print("Transfer aborted, invalid amount")

        to_account.deposit(amount)

    def add_money_to_account(self, amount):
        self.account.deposit(amount)



bank_acc = BankAccount("Joe Smith", 500.00)
print(bank_acc.get_balance())

#
# try:
#     bank_acc.withdraw(1000)
# except ValueError as e:
#     print("I was expecting an error and I caught it as expected")
#     assert e.args[0] == 'Insufficient funds'

ellie = BankUser("Ellie", "Skye", "D1234C55")
ellie.add_money_to_account(400)
ellie.wire(bank_acc, 50)

print(bank_acc.get_balance())

