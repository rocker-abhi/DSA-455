"""
    find the maximum consecutive ones
"""

def max_consecutive_ones(arr):
    max_count = 0 
    count = 0

    for i in range(0,len(arr)-1):
        if arr[i] == 1 :
            count += 1
            if count > max_count :
                max_count =  count
        else:
            count = 0
    return max_count

if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    print(f"maximum consecutive one's : {max_consecutive_ones(arr)}")