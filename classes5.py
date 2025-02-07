class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance")

acc = Account("John")
acc.deposit(100)
acc.withdraw(50)
acc.withdraw(60)
print(acc.balance)
