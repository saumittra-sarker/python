#class with attribute
# creating an instance of the class

import rlcompleter


class student: 
    def __init__(self,id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
student_info = student(1234,"Rohit",21)# istance
rolls = student.id_number()
print(rolls)