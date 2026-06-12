class Bank:
    def __init__(self,amount):
        self.amount = amount
    def getBalance(self):
        print("Current balance is:",self.amount)
    def getDeposit(self,amount):
        self.amount = self.amount + amount
    def withdraw(self,amount):
        self.amount = self.amount - amount

myobj = Bank(1000)
myobj.getBalance()
myobj.getDeposit(90000)
myobj.getBalance()
myobj.withdraw(100000)
myobj.getBalance()