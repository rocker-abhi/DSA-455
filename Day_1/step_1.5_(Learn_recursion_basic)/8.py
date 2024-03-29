"""
    check the string is palindrome or not .
"""

def check_pallindrome(string,p,q):
    if p > q :
        return True
    if string[p] == string[q] :
        p += 1
        q -= 1
        return check_pallindrome(string,p,q)
    else :
        return False

string = "abcdedcba"
p = 0
q = len(string)-1
if check_pallindrome(string,p,q) :
    print("This is a pallindrome")
else :
    print("This is not a pallindrome ")