from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking": BankAccount(int_rate=0.02, balance=0),
            "savings": BankAccount(int_rate=0.05, balance=0)
        }

    def make_deposit(self, amount, name):
        self.accounts[name].deposit(amount)
        return self

    def make_withdrawal(self, amount, name):
        self.accounts[name].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        for name, account in self.accounts.items():
            print(f"Account: {name}, Balance: {account.balance}")
        return self

user1 = User('Khaled', 'kh.es.abadla@gmail.com')
user2 = User('Bilal', 'bilal@gmail.com')

user1.make_deposit(100, 'checking').make_deposit(200, 'savings').make_withdrawal(50, 'checking').display_user_balance()
user2.make_deposit(1000, 'checking').make_deposit(500, 'savings').make_withdrawal(200, 'checking').make_withdrawal(100, 'savings').display_user_balance()