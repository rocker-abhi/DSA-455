"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
        1    1
        12  21
        123321

        Input Format: N = 6
        Result:   
        1          1
        12        21
        123      321
        1234    4321
        12345  54321
        123456654321
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-12-number-crown-pattern/
"""

def print_pattern(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            # loop to print the element on the left side
            print(j,end="")
        for _ in range(0, (rows-i)*2):
            print("",end=" ")
        for k in range(i,0,-1):
            print(k, end="")
        print()
                    
 
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(7)
