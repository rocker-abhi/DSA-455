"""
    code for selection sort . 
    
    W.T.C = n^2
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# Example usage:
arr = [7, 1, 4, 2, 3,87]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
