"""
    Problem Statement: Given an integer N, print the following pattern.
    
        Input Format: N = 3
        Result: 
        1
        2 3
        4 5 6

        Input Format: N = 6
        Result:   
        1
        2  3
        4  5  6
        7  8  9  10
        11  12  13  14  15
        16  17  18  19  20  21`
                     
    PROBLEM STATEMENT LINK : https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern/
"""

def print_pattern(rows):
    count = 1
    for i in range(1,rows+1):
        for j in range(0,i):
            print(count, end=" ")
            count += 1
        print()
 
if __name__ == "__main__":
    # num = int(input("Please enter the number : "))
    print_pattern(7)
