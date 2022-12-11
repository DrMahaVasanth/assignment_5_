# Challenge 3: Implement the complete student class
# Output: Student name is maha with the Roll No. 5
class student:
    
    def setName(self,_name):
        self._name=_name
    
    def getName(self):
        return self._name
    
    def setRollNumber(self,_rollNumber):
        self._rollNumber=_rollNumber
    
    def getRollNumber(self):
        return self._rollNumber
obj=student()
obj.setName("maha")
sname=obj.getName()
obj.setRollNumber("5")
srollno=obj.getRollNumber()
print(f"Student name is {sname} enrolled with the Roll No. {srollno}")


