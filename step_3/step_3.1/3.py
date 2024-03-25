"""
    check weather if the array is sorted or not 
"""

def check_array_is_sorted(arr):
    pivot = arr[0]
    
    for i in range(1, len(arr)-1) :
        if pivot > arr[i]:
            return False
    
    return True
    


if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    if check_array_is_sorted(arr):
        print("The array is sorted .")
    else:
        print("The array is not sorted .")
        

        