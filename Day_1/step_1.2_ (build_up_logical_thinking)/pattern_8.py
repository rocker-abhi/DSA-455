"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 8 : 
    
                ***********
                 *********
                  *******
                   ***** 
                    ***    
                     *
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-8-inverted-star-pyramid/
"""

def print_pattern(rows):
    for i in range(1,rows+1):
        for j in range(0,i):
            print("",end=" ")
        for k in range(rows+1-i,1,-1):
            print("*",end=" ")
        print()
            
if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)