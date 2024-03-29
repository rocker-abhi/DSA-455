"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 2 : 
    
            * 
            * * 
            * * *
            
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern/
"""

def print_pattern(num):

    for i in range(1,num+1):
        for j in range(0,i):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Please enter the integer :"))
    print_pattern(num)