"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 6 : 
    
            1 2 3 4 5 6
            1 2 3 4 5
            1 2 3 4
            1 2 3
            1 2 
            1
            
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-6-inverted-numbered-right-pyramid/
"""

def print_pattern(num):

    for i in range(num+1, 1, -1):
        for j in range(1, i):
            print(j,end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)