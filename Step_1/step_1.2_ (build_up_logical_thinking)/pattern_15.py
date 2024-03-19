"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Result: 
            A B C
            A B
            A

        Input Format: N = 6
        Result:   
            A B C D E F
            A B C D E 
            A B C D
            A B C
            A B
            A
                     
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern/
"""

def print_pattern(rows):
    # using the ascii code to print the character
    for i in range(rows,0,-1):
        for j in range(0,i):
            print(chr(65+j), end=" ")
        print("")
        
    
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(7)
