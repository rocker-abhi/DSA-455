"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
          A  
         ABA 
        ABCBA


        Input Format: N = 6
        Result:   
             A     
            ABA    
           ABCBA   
          ABCDCBA  
         ABCDEDCBA 
        ABCDEFEDCBA`
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-17-alpha-hill-pattern/
"""

def print_pattern(rows):
    # using the ascii code to print the character
    for i in range(1, rows+1):
        for j in range(0,rows-i+1):
            print(" " ,end="")
        for k in range(0,i):
            print(chr(65+k),end="")
        for l in range(i,1,-1):
            print(chr(65+l-2),end="")
        print()
    
               
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(6)
