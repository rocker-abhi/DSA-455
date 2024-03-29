"""
    reverse the number .
"""

num = 98765
num = str(num)
new_num = ""

for i in range (len(num)-1, 0, -1):
    new_num += num[i]

print(new_num)
    