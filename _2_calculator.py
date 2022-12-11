# Challenge 2: Implement a calculator class

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        self.added= self.num1+self.num2
        print(f"Sum of {self.num1} and {self.num2} is {self.added}")
    def subtract(self):
        self.subtracted= self.num2-self.num1
        print(f"Subtraction of {self.num1} from {self.num2} is {self.subtracted}")
    def multiply(self):
        self.multiplied= self.num1*self.num2
        print(f"Multiplied value of {self.num1} and {self.num2} is {self.multiplied}")
    def divide(self):
        self.divided= self.num2/self.num1
        print(f"Divided result of {self.num2} by {self.num1} is {self.divided}")
obj=calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

# Output:
# Sum of 10 and 94 is 104
# Subtraction of 10 from 94 is 84
# Multiplied value of 10 and 94 is 940
# Divided result of 94 by 10 is 9.4
