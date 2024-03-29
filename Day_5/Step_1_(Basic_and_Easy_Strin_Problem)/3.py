"""
    largest off string in the number .
"""

def largest_odd_number(string_input):
    # funtion to find the largest odd string in the string .
    n = len(string_input)-1
    
    while n >= 0 :
        if int(string_input[n]) % 2 == 0 :
            n -= 1 
            string_input = string_input[:-1]
        else :
            break
    return string_input
    
if __name__ == "__main__" :
    string_input = str(input("please enter string :"))
    num = largest_odd_number(string_input)
    if len(num) > 0 :
        print(num)
    else:
        print('""')