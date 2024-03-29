"""
    Sort an array of 0s, 1s and 2s
"""

def sort_array(arr):
    count_0 = []
    count_1 = []
    count_2 = []
    
    for num in arr:
        if num == 0 :
            count_0.append(0)
        elif num == 1:
            count_1.append(1)
        else:
            count_2.append(2)
    return count_0 + count_1 + count_2

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    result = sort_array(nums)
    print(result)