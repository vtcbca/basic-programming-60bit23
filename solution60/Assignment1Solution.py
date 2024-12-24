from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Test the function
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial_reduce(number)}")
