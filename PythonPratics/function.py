# Python Functions

# creating a function and calling

def gratting():
    print("Hey there!")


gratting()


# Arguments passing
def gratting(fname):
    print(" fruits name is " + fname)


fruits=["Avocado", "Banana", "Apple", "Mango", "Kiwi", "Orange", "Pineapple", "Watermelon", "Lemon", "Apricot", "Blueberry", "Plum", "Cherry", "Fig", "Papaya", "Grapefruit", "Strawberry"]
length=len(fruits)
print(length)
startingIndex=0

while startingIndex <= length:
    gratting(fruits[startingIndex])
    startingIndex += 1


