"""
    check weather the string is a plandrome .
"""

def check_pallindrome(string_input):
    is_pallindrome = True
    q = len(string_input)-1
    p = 0
    
    while p < q :
        if string_input[p] == string_input[q]:
            p += 1 
            q -= 1
        else:
            is_pallindrome = False
            break
    
    return is_pallindrome
    
    

if __name__ == "__main__" :
    string_input = str(input("please enter string :"))
    if check_pallindrome(string_input):
        print("This is a pallindrome .")
    else:
        print("This is not a pallindrome .")
