"""
    This code for the bubble sort .
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                
    return arr
    
# Example usage:
arr = [7, 1, 4, 2, 3,87]
sorted_arr = bubble_sort(arr)
print("Bubbled sort array is:", sorted_arr)