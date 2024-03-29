"""
    Kadane’s Algorithm : Maximum Subarray Sum in an Array
"""

def kadane_algorithm(nums):
    max_so_far = max_end_here = nums[0]
    
    for i in nums[1:]:
        max_end_here = max(i, max_end_here + i)
        max_so_far = max(max_so_far, max_end_here)
    
    return max_so_far

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4] 
    print(kadane_algorithm(arr))