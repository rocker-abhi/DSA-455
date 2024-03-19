"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 10 : 
        Input Format: N = 3
        Result: 
        1
        01
        101

        Input Format: N = 6
        Result:   
        1
        01
        101
        0101
        10101
        010101
            *
                     
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern/
"""

def print_pattern(rows):
    for i in range(1, rows+1):
        for j in range(1,i+1):
            if i%2 == 1:
                # row is odd
                if j%2==0:
                    # column is odd
                    print("0",end=" ")
                else:
                    print("1",end=" ")
            else:
                # row is even
                if j%2==0:
                    # column is odd
                    print("1",end=" ")
                else:
                    print("0", end=" ")
        print()
                    
 
if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)
