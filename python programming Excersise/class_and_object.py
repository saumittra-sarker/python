#class and objects

#create class
class person: # person is a class
    #body of class
    first_name = "Saumittra"
    last_name = "Sarker"
    age = 29
person_object = person()#class object

#access properties
first_name = person_object.first_name
last_name = person_object.last_name
age = person_object.age

print("First name is: ",first_name)
print("First name is: ",last_name)
print("First name is: ",age)