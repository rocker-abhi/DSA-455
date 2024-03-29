"""
    move zero's at the end of the arry .
"""

def move_zero_at_end(arr):
    arr_without_zero = []
    arr_with_zero = []
    
    for num in arr :
        if num != 0 :
            arr_without_zero.append(num)
        else:
            arr_with_zero.append(num)
    arr = arr_without_zero + arr_with_zero
    return arr
    
    
if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    arr = move_zero_at_end(arr)
    print(f'all zero move at the end of the arr : {arr}')