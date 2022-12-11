# Challenge 1: Square numbers and return their sum
# Output: Sum of Squares for 1,3 and 5 is 35
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sq_sum(self):
        self.sum_of_squares= self.x**2+self.y**2+self.z**2
        print(f"Sum of Squares for {self.x},{self.y} and {self.z} is {self.sum_of_squares}")
obj=point(1,3,5)
obj.sq_sum()
