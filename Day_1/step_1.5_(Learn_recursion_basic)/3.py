"""
    Print 1 to N using Recursion
"""

def print_number(number):
    if number > 0 :
        print_number(number-1)
        print(number)
    

if __name__ == "__main__":
    print_number(10)