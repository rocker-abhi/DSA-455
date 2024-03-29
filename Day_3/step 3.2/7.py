"""
    Rearrange Array Elements by Sign
"""

def arrange_array(nums):
    
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if i % 2 == 0 :
                if nums[j] > 0 :
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                if nums[j] < 0 :
                    nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == "__main__":
    n = int(input("Please enter the size of the array :"))
    nums = []
    for i in range(0, n):
        item = int(input("please enter the item :"))
        nums.append(item)
    nums = arrange_array(nums)
    print(nums)