"""
    recursive bubble sort .
"""

def bubble_sort(arr, n):
    if n == 1:
        return arr

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1], arr[i]

    return bubble_sort(arr, n-1)

arr = [7, 1, 4, 2, 3,87]
sorted_arr = bubble_sort(arr,len(arr))
print("Bubbled sort array is:", sorted_arr)