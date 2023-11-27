class BankAcount():
    def __init__(self):
        self.balance = 0
    def deposite(self, amount):
        self.balance+=amount
        return self.balance
    def withdrawl(self, amount):
        self.balance-=amount
        return self.balance
    def info(self):
        print(f"Account balance: {self.balance}")

acount = BankAcount()
print(acount.deposite(1000))
# print(acount.witdrawl(200))
print(acount.withdrawl(500))
acount.info()