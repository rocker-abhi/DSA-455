"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
        1
        2 3
        4 5 6

        Input Format: N = 6
        Result:   
        A
        A B
        A B C
        A B C D
        A B C D E
        A B C D E F
                     
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern/
"""

def print_pattern(rows):
    # using the ascii code to print the character
    for i in range(1, rows+1):
        for j in range(0, i):
            print(chr(65+j),end="")
        print()
 
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(7)
