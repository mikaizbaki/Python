class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money!")

    def display_balance(self):
        print(self.balance)

        acc = BankAccount("James", 100)
        acc.deposit(50)
        acc.display_balance()

