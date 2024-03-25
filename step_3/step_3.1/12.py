"""
    The number that is appearing one's
"""

def appear_one_time(arr):
    appearig_ones = []
    
    for i in range(0, len(arr)):
        count = 0
        for j in range(0,len(arr)):
            if i == j :
                continue
            elif arr[i] == arr[j]:
                count += 1
        if count == 0 :
            appearig_ones.append(arr[i])
    
    return appearig_ones


if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    print(f"The num that is appearing ones : {appear_one_time(arr)}")