"""
    Problem Statement: Given an integer N, print the following pattern.
    
    PATTERN 5 : 
    
            1
            2 2
            3 3 3
            4 4 4 4
            5 5 5 5 5
            6 6 6 6 6 6
            
    PROBLEM STATEMENT LINK :https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii/
"""

def print_pattern(num):

    for i in range(1,num+1):
        for j in range(0,i):
            print(i,end=" ")
        print()

if __name__ == "__main__":
    num = int(input("Please enter the number : "))
    print_pattern(num)