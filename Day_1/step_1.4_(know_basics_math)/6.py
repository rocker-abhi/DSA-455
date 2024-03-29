"""
    print all divisor's
"""

number = int(input("Please enter the number : "))

for i in range(1, number+1):
    if number % i == 0:
        print(i, end=" ")