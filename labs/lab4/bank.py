print("Bank")

class Accounting:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposit +{amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.history.append(f"Failed withdraw {amount}")
            return "You don't have enough money"
        else:
            self.balance -= amount
            self.history.append(f"Withdraw -{amount}")
            return self.balance

    def show_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        if amount > self.balance:
            self.history.append(f"Failed transfer {amount}")
            return "You don't have enough money"
        else:
            self.balance -= amount
            other_account.balance += amount

            self.history.append(f"Transfer to {other_account.name} -{amount}")
            other_account.history.append(f"Transfer from {self.name} +{amount}")

            return "Transfer successful"

    def show_history(self):
        for h in self.history:
            print(h)


one = Accounting("one", 100)
two = Accounting("two", 200)

one.deposit(50)
one.withdraw(30)
one.transfer(two, 20)

print("Balance:", one.show_balance())
print("History:")
one.show_history()
