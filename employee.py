import random

class Employee:
    def __init__(self,name):
        self.name=name
        self.is_Present=False
    
    def check_attendance(self):
        attendance=random.randint(0,1)
        if attendance==1:
            self.is_Present=True
            print(f"{self.name} is Present")
        else:
            self.is_Present=False
            print(f"{self.name} is Absent")

    