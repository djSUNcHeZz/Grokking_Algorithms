# Recursion factorial

def factorial(x):
    return x if x == 1 else x * factorial(x - 1)


print(factorial(int(input("Factorial: "))))
