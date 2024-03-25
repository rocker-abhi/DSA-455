"""
    code to fint the linear search
"""

def linear_serach(arr, num_to_search):
    index = None
    for i in range(0,len(arr)-1) :
        if arr[i] == num_to_search:
            index = i
    
    print(index)
    return index
            
    
if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(0,size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
    
    num_to_search = int(input("please enter the number to search: "))
    
    index = linear_serach(arr, num_to_search)
    
    if index is None:
        print(f'{num_to_search}, in not found')
    else:
        print(f'{num_to_search}, found at index {index}')