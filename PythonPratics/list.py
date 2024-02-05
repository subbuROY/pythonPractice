# Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
tropical = ["mango", "pineapple", "custed Apple"]
print(thislist, "\n")
# access list

print(thislist[0], '\n')
print(thislist[-1], '\n')  # -ve index make the ending line of  index
# Change Item Value
# Insert Items
thislist[0] = "watermelon"
print(thislist, '\n')
# Insert Items another way
thislist.insert(0,"apple")

# Python - Add List Items
thislist.append("papaya")
print(thislist, '\n')
thislist.extend(tropical)
print(thislist, '\n')

# Remove Specified Item
thislist.remove("papaya")





