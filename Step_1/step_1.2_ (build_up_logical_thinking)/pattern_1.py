"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 1 : 
    
            * * * * * *
            * * * * * *
            * * * * * *
            * * * * * *
            * * * * * *
            * * * * * *
            
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern/
"""

def print_pattern(num):
    # This function accepts the single argument 
    
    for i in range(0,num):
        for j in range(0,num):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    # This is the driver code 
    num = int(input("Please enter the number :")) # line take's the input 
    print_pattern(num)  # printing the pattern 1 
