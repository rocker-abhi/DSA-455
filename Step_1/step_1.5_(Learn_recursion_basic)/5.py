"""
    sum of first n numbers .
"""

def sum_of_number(number):
    if number == 1 :
        return 1 
    return number + sum_of_number(number-1)

sum = sum_of_number(10)
print(sum)