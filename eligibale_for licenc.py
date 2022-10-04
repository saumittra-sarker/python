user_age = int(input("Enter your age"))

if user_age>=18 and user_age<=45:
    print("You are Eligible for driving license")
elif user_age>=45 and user_age<=65:
    print("You are elegible for driving license but chances is low")
elif user_age<18:
    print("Your age is less than 18, so are not eligible for Driving license, ")
else:
    print("45")