class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance = 0

  def make_deposit(self, amount):
    self.balance += amount

  def make_withdrawal(self, amount):
    if self.balance < amount:
      print("Your balance is not enough to withdraw")
      return False
  
    self.balance -= amount
    

  def transfer_money(self, reciepent, amount):
    if(self.balance < amount):
      print("Your balance is not enough to withdraw")
      return False

    self.balance -= amount
    reciepent.balance += amount
    print(f"{self.name} balance is: {self.balance}")
    print(f"{reciepent.name} balance is: {reciepent.balance}")


user1 = User("Khaled Alabadla", "kh.es.abadla@gmail.com")
user2 = User("Bilal Qanoa", "bilalqanoa@gmail.com")
user3 = User("Salah Ahmed", "salahahmed@gmail.com")

user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_withdrawal(300)
print(f"Net balance of {user1.name} is {user1.balance}")

user2.make_deposit(100)
user2.make_deposit(200)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
print(f"Net balance of {user2.name} is {user2.balance}")

user3.make_deposit(300)
user3.make_withdrawal(200)
user3.make_withdrawal(200)
user3.make_withdrawal(200)
print(f"Net balance of {user3.name} is {user3.balance}")

user1.transfer_money(user2, 200)

