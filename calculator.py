num1 = input("Enter your 1st Number: ")
operation = input("Enter your operator'+,-,*,/' : ")
num2 = input("Enter your 2nd Number: ")

if operation == '+':
    result = int(num1) + int(num2)
    print(num1,"+",num2,"=",result)
elif operation == '-':
    result = int(num1) - int(num2)
    print(num1,"-",num2,"=",result)
elif operation == '*':
    result = int(num1) * int(num2)
    print(num1,"x",num2,"=",result)

elif operation >0 and operation == '/':
    result = int(num1) / int(num2)
    print(num1,"/",num2,"=",result)
else:
    print("Something is error")
