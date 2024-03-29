"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 9 : 
    
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-9-diamond-star-pattern/
"""

def print_pattern(rows):
    """
        steps:
        1. solve the upper part firstly.
        2. solve the lower part secondly.
    """
    for i in range(1,rows+1):
        """
            This for loop is for the upper part .
        """
        for j in range(0, rows-i):
            # loop is for the adding the space  .
            print("", end=" ")
        for k in range(0,i):
            # loop is for add the * .
            print("*", end=" ")
        print()
        
    for i in range(rows+1,1,-1):
        """
            This loop is for the bottom part .
        """
        for j in range(0, rows-i+1):
            # loop is for adding the space
            print("",end=" ")
        for k in range(1,i):
            # loop is for add the * 
            print("*",end=" ")
        print()
        
         
if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)