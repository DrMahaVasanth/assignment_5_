# Challenge 5: Implement a Bank management system
class account:
    
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    
    def withdrawl(self,amount):
        self.balance-=amount
    
    def deposit(self,amount):
        self.balance+=amount
    
    def getBalance(self):
        return self.balance

class savingsaccount(account):
    
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate
    
    def interestAmount(self):
        self.interest_amount=self.interestRate*self.balance/100
        print(f"Calculated interest amount for {self.title} with {self.interestRate}% as the interest rate is {self.interest_amount}")

obj=savingsaccount("Maha",2000,5)
print("Initial balance amount:",obj.getBalance())
obj.withdrawl(500)
print("Balance after withdrawl",obj.getBalance())
obj.deposit(500)
print("Balance after deposit",obj.getBalance())
obj.interestAmount()

