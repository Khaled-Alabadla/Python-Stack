class BankAccount:
    """A class to represent a bank account with interest rate and balance."""
    def __init__(self, int_rate, balance): 
        # Initialize interest rate and initial balance
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        """Increase the account balance by the given amount."""
        self.balance += amount
        return self

    def withdraw(self, amount):
        """Decrease the account balance by the given amount if funds are available."""
        if(self.balance < amount):
          return False

        self.balance -= amount
        return self

    def display_account_info(self):
        """Print the current balance of the account."""
        print(f"The net balance is {self.balance}$")

    def yield_interest(self):
        """Add interest to the account balance based on the interest rate."""
        self.balance += (self.balance * self.int_rate)
        return self

account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.05, 3000)

account1.deposit(100).deposit(200).deposit(300).withdraw(300).yield_interest().display_account_info()
account2.deposit(1000).deposit(200).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()