f = open(r"df.txt","r")
reads = f.read()

x1 = f.readline()
x2 = f.readline()
x3 = f.readline()
print(x1)
print(x2)
print(x3)


f.close()