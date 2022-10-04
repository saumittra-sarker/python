#-------------- Chapter - 06 List---------------
# lidt is a ordered container
# Create a list 

from time import perf_counter


#pets = ["Dog","Cat","Rabit"] # 
#p#rint("Old list", pets)
#print(pets) 


#---->> Indexing
#print(pets[2])# positive indexing start at "0", 1,2,3,.....
#print(pets[0]) # ACCESS 1ST elements


#---->> Negative Indexing
#print(pets[-3])

#---->> Range of Indexing
#print(pets[1:3])
#---- >>> Adding Items to a list
#.append functions
#pets.append("Elephent")
#print(pets)

#insert functions

#pets.insert(0,"elephent")
#print(pets)
#--- >> Deleting items from a list
#pets.pop()# last item delete
#print(pets)#
#pets.remove("Cat")
#print(pets)

#--- Getting the lrngth of list
#print(len(pets))


#---- changing an item
#pets[1] = "Fish"
#print(pets)

#extending list

#num = [1,2,3,4]
#num2 = [5,6,7,8]
#num.extend(num2)
#print(num)


#---- Cheak is an itam exist


# membership operator

# membership operator are two type 1. in and 2. not in


country = ["India", "Bangladesh", "Australia", "England"]
check_item = "Australia" not in country
print(check_item)