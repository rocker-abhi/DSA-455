"""
    Factorial of a Number : Iterative and Recursive
"""

def factorial(number):
    if number == 1 :
        return 1
    return number * factorial(number-1)

result = factorial(5)
print(result)