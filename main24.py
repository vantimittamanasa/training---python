class account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accn0=accno
    def debit(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"{amount}is debited,bal is{self.getbal()}")
        else:
            print("insufficient funds")
    def credit(self,amount):
            self.balance+=amount
            print(f"{amount}is credited,bal is{self.getbal}")
    def getbal(self):
        return self.balance
acc1=account(1000,"acc123")
acc1.credit(500)
acc1.debit(1000)