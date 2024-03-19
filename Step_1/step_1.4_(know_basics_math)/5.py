"""
    armstrong number .
"""

num = int(input("please enter the number :"))
num = str(num)
num_digit = len(num)
result = 0

for digit in num:
    # square of the number
    result += int(digit) ** num_digit

if num == digit :
    print("This is a armstrong number .")
else:
    print("This is not a armstrong number .")