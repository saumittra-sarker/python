#f = open("file.txt","x")#syntax- open("filename with location","file operation")
#operation part
# to create a file
#f.close()



#writing something on python file
# syntax- open("filename","w")
#f = open("file.txt","w")
#f.write("I love python programming")
#f.close()

# adding anather line on created file

#f = open("file.txt","a")

#f.write(" and JavaScript also")

#f.close()

#read a file and print on terminal

#f = open("file.txt", "r")
#x = f.read()
#print(x)
#f.close()

#f = open("file.txt","r")
#first_line = f.readline()
#s_line = f.readline()

#print(first_line)
#print(s_line)
#f.close()

import os

os.remove("delete.txt")
f = open("delete.txt", "r")
f.close()
