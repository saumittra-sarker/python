#class person:
    #firs_name = "Saumittra"
    #last_name = "Sarker"
    #age = 29
#person_obj = person()
#f_name = person_obj.firs_name
#l_name = person_obj.last_name
#age = person_obj.age

#print("your first name is: ",f_name)
#print("You last name is: ", l_name)
#print("Your age is: ", age)

#class with attributes
#creating an instances of the class
class student:
    def __init__(self,id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
    def student_greet(self):# mathode call
        print("hello",self.name, ", Hou are you?")
student1 = student(1234, "Rohit",21)#instances
student2 = student(1235, "Saumittra Sarker", 29)

x1 = student1.id_number
x2 = student1.name
x3 = student1.age

print("Student ID Number is: ", x1)
print("Student Name is: ", x2)
print("Student age is: ", x3)
student2.student_greet()
print("Student ID Number is: ", student2.id_number)
print("Student Name is: ", student2.name)
print("Student age is: ", student2.age)
