"""
    left rotate the array by d places
"""

def left_rotate_array_by_x(arr, rotate_by):
    
    for i in range(0, rotate_by):
        temp = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp
        
    return arr
    
    
if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
    
    rotate_by = int(input("arr rotate by place"))
    
    arr = left_rotate_array_by_x(arr, rotate_by)
    
    print(f"rotated arr : {arr}")