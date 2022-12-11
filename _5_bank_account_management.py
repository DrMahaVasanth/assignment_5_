# Challenge 5: Implement a Bank management system
class account:
    
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    
    def withdrawl(self,amount):
        self.balance-=amount
    
    def deposit(self,amount):
        self.balance+=amount
    
    def get_balance(self):
        return self.balance

class savingsaccount(account):
    
    def __init__(self,title=None,balance=0,interest_rate=0):
        super().__init__(title,balance)
        self.interest_rate=interest_rate
    
    def interest_amount(self):
        self.interest_amount=self.interest_rate*self.balance/100
        print(f"Calculated interest amount for {self.title} with {self.interest_rate}% as the interest rate is {self.interest_amount}")

obj=savingsaccount("Maha",2000,5)
print("Initial balance amount:",obj.get_balance())
obj.withdrawl(500)
print("Balance after withdrawl",obj.get_balance())
obj.deposit(500)
print("Balance after deposit",obj.get_balance())
obj.interest_amount()

