"""
    Print N to 1 using Recursion
"""

def print_number(number):
    print(number)
    if number == 1 :
        return
    print_number(number-1)

if __name__ == "__main__":
    print_number(10)