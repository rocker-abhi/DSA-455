"""
    1Find the highest/lowest frequency element
    
    Example 1:
    Input: array[] = {10,5,10,15,10,5};
    Output: 10 15
    Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

    Example 2:

    Input: array[] = {2,2,3,4,4,2};
    Output: 2 3
    Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
"""
def most_and_least_frequent(arr):
    frequency = {}  # Dictionary to store the frequency of elements

    # Count occurrences of each element in the list
    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    # Find the item with the highest and lowest frequencies
    max_frequency_item = max(frequency, key=frequency.get)
    min_frequency_item = min(frequency, key=frequency.get)

    return max_frequency_item, min_frequency_item

arr = [2,2,3,4,4,4,4,2]
max, min = most_and_least_frequent(arr)
print(min, end=" ")
print(max, end=" ")
