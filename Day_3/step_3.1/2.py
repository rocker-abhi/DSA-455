"""
    find the second smallest and the second largest element in the array .
"""

def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        p = q = r = 0 
        while p < len(left_arr) and q < len(right_arr) :
            if left_arr[p] < right_arr[q]:
                arr[r] = left_arr[p]
                r += 1
                p += 1
            else:
                arr[r] = right_arr[q]
                r += 1
                q += 1
        
        while p < len(left_arr) :
            arr[r] = left_arr[p]
            r += 1
            p += 1
        
        while q < len(right_arr) :
            arr[r] = right_arr[q]
            r += 1
            q += 1
        
        return arr
        

if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
        
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    
    print(f'second smallest element in the array : {sorted_arr[1]}')
    print(f'second largest element of the array : {sorted_arr[-2]}')
        
        