def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = int(input("Enter the finding factorial number:-"))
result = factorial_recursive(number)
print(f"the factorial number of {number}\n is \n {result}")
