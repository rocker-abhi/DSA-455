"""
    Find the Majority Element that occurs more than N/2 times
"""

def function(nums):
    n = len(nums)/2
    result = []
    for i in range(0,len(nums)-1):
        count = 0
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                count += 1
                if n <= count:
                    result.append(nums[i])
                    break
            if len(result) == 1:
                break
        if len(result) == 1:
            break
    return result

if __name__ == "__main__":
    n = int(input("please enter the size : "))
    nums = []
    
    for i in range(0, n):
        item = int(input("Please enter the item : "))
        nums.append(item)
    
    result = function(nums)
    print(result)
    