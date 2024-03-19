"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
        A
        B B
        C C C

        Input Format: N = 6
        Result:   
        A 
        B B
        C C C
        D D D D
        E E E E E
        F F F F F F
                     
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern/
"""

def print_pattern(rows):
    # using the ascii code to print the character
    for i in range(0,rows+1):
        for j in range(0,i):
            print(chr(65+i-1),end=" ")
        print()        
    
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(6)
