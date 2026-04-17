# Class representing a User with a bank balance
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance = 0

  # Deposit money and return self to allow chaining
  def make_deposit(self, amount):
    self.balance += amount
    return self

  # Withdraw money and return self to allow chaining
  def make_withdrawal(self, amount):
    if self.balance < amount:
      print("Your balance is not enough to withdraw")
      return False

    self.balance -= amount
    return self


  # Transfer money between user objects
  def transfer_money(self, reciepent, amount):
    if(self.balance < amount):
      print("Your balance is not enough to withdraw")
      return False

    self.balance -= amount
    reciepent.balance += amount
    print(f"{self.name} balance is: {self.balance}")
    print(f"{reciepent.name} balance is: {reciepent.balance}")


# Create User instances
user1 = User("Khaled Alabadla", "kh.es.abadla@gmail.com")
user2 = User("Bilal Qanoa", "bilalqanoa@gmail.com")
user3 = User("Salah Ahmed", "salahahmed@gmail.com")

# Demonstrate method chaining
user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(300)

print(f"Net balance of {user1.name} is {user1.balance}")

# Another example of chaining
user2.make_deposit(10000).make_deposit(20000).make_withdrawal(100).make_withdrawal(100)
print(f"Net balance of {user2.name} is {user2.balance}")

# Chaining multiple withdrawals
user3.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200)
print(f"Net balance of {user3.name} is {user3.balance}")

# Regular method call (no chaining demonstrated here)
user1.transfer_money(user2, 200)

