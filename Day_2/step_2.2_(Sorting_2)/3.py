def recursive_insertion_sort(arr, n):
    # Base case: if array has only one element or empty, it's already sorted
    if n <= 1:
        return

    # Sort first n-1 elements recursively
    recursive_insertion_sort(arr, n - 1)

    # Insert last element at its correct position in sorted array
    last_element = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..i-1], that are greater than key,
    # to one position ahead of their current position
    while j >= 0 and arr[j] > last_element:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last_element

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
recursive_insertion_sort(arr, len(arr))
print("Sorted array is:", arr)
