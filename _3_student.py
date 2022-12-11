# Challenge 3: Implement the complete student class
# Output: Student name is maha with the Roll No. 5
class student:
    
    def set_name(self,_name):
        self._name=_name
    
    def get_name(self):
        return self._name
    
    def set_roll_no(self,_roll_no):
        self._roll_no=_roll_no
    
    def get_roll_no(self):
        return self._roll_no

obj=student()
obj.set_name("maha")
sname=obj.get_name()
obj.set_roll_no("5")
srollno=obj.get_roll_no()
print(f"Student name is {sname} enrolled with the Roll No. {srollno}")


