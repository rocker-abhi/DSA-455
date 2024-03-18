"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 3 : 
    
            1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5
            1 2 3 4 5 6
            
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-3-right-angled-number-pyramid/
"""

def print_pattern(num):

    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)