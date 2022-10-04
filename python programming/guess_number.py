import random

mynum = random.randint(0,9) #random number by computer
print("I have a number in my mind, can you guess it? ")

while True:
    userNumber = int(input("enter your namber: "))
    if userNumber == mynum :
        print("You are right")
        break
    elif userNumber > mynum:
        print("My number is grater than the number you entered, \ntry again")
    else:
        print("my number is less than the number you entered, \ntry again")
