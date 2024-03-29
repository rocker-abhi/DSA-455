"""
    Longest Subarray with given Sum K(Positives)
"""

def find_the_sum(arr, sum):
    arr_list = []
    for i in range(0,len(arr)):
        arr_list = []
        sum_of_item = 0
        for j in range(i,len(arr)):
            sum_of_item += arr[j]
            arr_list.append(arr[j])
            if sum_of_item == sum :
                break
        if sum_of_item == sum:
            break
    return arr_list
            


size_of_arr = int(input("please enter the size of the array : "))
arr = []
for i in range(size_of_arr):
    arr.append(int(input("enter the item in the array : ")))
k = int(input("sum to find : "))

result = find_the_sum(arr,k)
print(result)