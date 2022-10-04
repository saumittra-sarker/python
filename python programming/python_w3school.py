#accessing set

sets={"apple", "banana", "cherry"}


print("banana" in sets)

sets.add("orange")
print(sets)

setn = {"pineapple", "mango", "papaya"}
sets.update(setn)
print(sets)

lists= ["kiwi", "orange"]
sets.update(lists)
print(sets)