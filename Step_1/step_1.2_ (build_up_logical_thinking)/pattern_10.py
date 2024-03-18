"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 9 : 
        Input Format: N = 3
        Result: 
            *  
            **
            ***  
            **
            *   
            
        Input Format: N = 6
        Result:   
            *
            **
            *** 
            ****
            *****
            ******  
            *****
            ****
            ***    
            **
            *
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern/
"""

def print_pattern(rows):
    """
        steps:
        1. solve the upper part firstly.
        2. solve the lower part secondly.
    """
    for i in range(1,rows+1):
        for j in range(0,i):
            print("*",end="")
        print()
    
    for i in range(rows,1,-1):
        for j in range(i,1,-1):
            print("*",end="")
        print()
        
         
if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)