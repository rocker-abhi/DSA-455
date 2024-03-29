"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
            C
            B C
            A B C

        Input Format: N = 6
        Result:   
            F
            E F
            D E F
            C D E F
            B C D E F
            A B C D E F
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-18-alpha-triangle-pattern/
"""

def print_pattern(rows):
    for i in range(1,rows+1):
        for j in range(i,0,-1):
            print(chr(65+rows-j),end=" ")
        print()
    
               
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(7)
