# Challenge 4: Implement a banking account
# TASKS
# 1. Parent class-account; child class - savingsaccount
# 2. Implement properties (account class - title and balance; savingsaccount class - interestrate) as instance variables and set them to None and 0
# 3. create initializer for account class 
#    create initializer for savingsaccount class using account class initializer
class account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class savingsaccount():
    def __init__(self,title=None,balance=0,interest_rate=0):
        super().__init__(title,balance)
        self.interest_rate=interest_rate

