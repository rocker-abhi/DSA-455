"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 4 : 
    
            * * * * * *
            * * * * * 
            * * * * 
            * * * 
            * * 
            * 
            
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid/
"""

def print_pattern(num):

    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)