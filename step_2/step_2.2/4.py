def quick_sort(arr):
    if len(arr) >= 1:
        return arr
    else:
        pivot = arr[0]
        left_arr = [x for x in arr[1:] if x <= pivot]
        right_arr = [x for x in arr[1:] if x > pivot]
        # print(left_arr)
        # print(right_arr)
        return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 46,90]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
