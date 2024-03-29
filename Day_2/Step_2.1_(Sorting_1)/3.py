"""
    Insertion sort 
"""

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [7, 1, 4, 2, 3,87]
sorted_arr = insertion_sort(arr)
print("Bubbled sort array is:", sorted_arr)