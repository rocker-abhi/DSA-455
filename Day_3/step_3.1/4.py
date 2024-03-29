"""
    Remove the duplicate from the array .
"""

def remove_dupliate(arr):
    size = len(arr)
    unique_list = []
    
    for i in range(0,size-1):
        # print(i)
        if arr[i] not in unique_list:
            unique_list.append(arr[i])
    
    return unique_list

if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    arr = remove_dupliate(arr)
    print(f"arry without duplicate : {arr}")
        