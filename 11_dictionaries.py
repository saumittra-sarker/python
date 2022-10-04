#---- Chapter 11- dictionary in python 

'''
    dictionary_name = {
        key:value,
        key:value,
    }
'''
#creating a dictionary
person ={
    "first_name":"John",
    "last_name":"Doe",
    "age":30
}
#print(person)
#print(type(person))



#accessing item
#x = person["first_name"]# dictinoary [key]
#y = person["last_name"]
#z = person["age"]
#a = person["hobby"]
#print("First Name: ", x)
#print("Last Name: ", y)
#print("Age: ", z)
#print("your hobby: ",a)


#get() methode

#get_methde= person.get("first_name")
#print(get_methde)
#adding new item
person["hobby"] = "Batmention"
print(person)
#changing an item's value
person["first_name"] = "Saumittra"
print(person)

#removing an item value
person.pop("hobby")
print(person)

#nestted dic
employe_data = {
    "manager":{
        "name": "Saumittra",
        "age":20
    },
    "programmer":{
        "name":"Ratna",
        "age":25
    },
    "salary": {
        "manager_salary": 45000,
        "programmer_salary": 39000,

    }
}
#print manager name and salary
print("manager name is: ", employe_data["manager"]["name"],
 "Manager age is:", employe_data["manager"]["age"],
 "Manager salary is: ", employe_data ["salary"]["manager_salary"])

print("Programmer name is: ", employe_data["programmer"]["name"],
 "Manager age is:", employe_data["programmer"]["age"],
 "Manager salary is: ", employe_data ["salary"]["programmer_salary"])