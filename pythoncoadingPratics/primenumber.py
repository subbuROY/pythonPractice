# This program belongs to given number is prime or not
print("Hey There!")

number = int(input("Enter your Number:-"))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is  a not prime number")
            break
    else:
        print(number, " is prime number")

else:
    print(number, "is not a prime number")

