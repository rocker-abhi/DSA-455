"""
    Count Subarray sum Equals K
"""

def sub_array_sum(array, target):
    sub_array = []
    
    for i in range(len(nums)-1):    
        sum = array[i]
        sub_array = []
        sub_array.append(array[i])
        for j in range(i+1, len(array)):
            sum = sum + array[j]
            sub_array.append(array[j])
            if sum > target :
                break
            if sum == target :
                break
    return sub_array  

if __name__ == "__main__":
    n = int(input('please enter the array size :'))
    nums = []
    
    for i in range(n):
        item = int(input("please enter the number : "))
        nums.append(item)
    
    target = int(input("please enter target to find :"))
    ary = sub_array_sum(nums, target)
    print(len(ary))