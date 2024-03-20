"""
    Print Name N times using Recursion
"""

def print_name(num):
    if num == 0 :
        return
    print("my name is Abhishek .")
    print_name(num-1)

if __name__ == "__main__":
    print_name(25)