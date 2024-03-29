"""
    next_permutaitons
"""

def next_permutation(nums):
    # Step 1: Find the largest index i such that nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    # If no such index exists, it means it's the last permutation
    if i == -1:
        return None
    
    # Step 2: Find the largest index j greater than i such that nums[j] > nums[i]
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    # Step 3: Swap the elements at indices i and j
    nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the sublist from i+1 to the end of the list
    nums[i+1:] = reversed(nums[i+1:])
    
    return nums

# Example usage:
nums = [2, 1, 3]
next_perm = next_permutation(nums)
if next_perm:
    print("Next permutation:", next_perm)
else:
    print("No next permutation exists.")
