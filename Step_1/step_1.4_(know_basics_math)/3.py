"""
    check the pallindrome .
"""

num = 12321
num = str(num)
p = 0
q = len(num)-1
is_pallindrome = True

while p < q :
    if num[p]==num[q]:
        p += 1
        q -= 1
    else:
        is_pallindrome = False
        break

if is_pallindrome:
    print("this is the pallindrome.")
else:
    print("this is not a pallindrome. ")