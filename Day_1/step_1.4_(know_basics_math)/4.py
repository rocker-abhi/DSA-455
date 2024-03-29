"""
    find the GCD of two number .
"""

num_1 = 3
num_2 = 6
greatest_divisor = 1

for i in range(2, num_2-1):
    if ((num_1 % i == 0)and(num_2 % i == 0 )):
        greatest_divisor = i

print(f"G.C.D = {greatest_divisor}")