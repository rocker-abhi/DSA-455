"""
    left rotate the array by one
"""

def left_rotate_array(arr):
    temp = arr[0]
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp
    return arr


if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
    
    arr = left_rotate_array(arr)
    print(f"Left rotated array is : {arr}")