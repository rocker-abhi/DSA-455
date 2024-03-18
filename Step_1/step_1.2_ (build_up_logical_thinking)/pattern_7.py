"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 7 : 
    
                 *     
                ***    
               *****   
              *******  
             ********* 
            ***********
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-7-star-pyramid/
"""

def print_pattern(rows):

    for i in range(1, rows+1):
        
        for j in range(1, rows-i+1):
            print("", end=" ")     
        for k in range(0,i):
            print("*", end=" ")
        print()
             

if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(5)