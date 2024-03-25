"""
    print the missing num
"""

def print_the_missing(arr):
    for i in range(0, len(arr)-1) :
        if arr[i+1]- arr[i] > 1:
            print(f"missing : {arr[i]+1}")
    
    
if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
    print_the_missing(arr)