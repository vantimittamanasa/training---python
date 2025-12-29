class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} debited, balance is {self.balance}")
        else:
            print("Insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited, balance is {self.balance}")

    def getbal(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, interest):
        self.interest = interest
        super().__init__(1000, "acc123")

    def interestrate(self):
        interest1 = self.balance * (self.interest / 100)
        self.balance += interest1
        print("Balance after interest:", self.getbal())


# object creation
acc1 = SavingsAccount(5)
acc1.credit(500)
acc1.interestrate()
