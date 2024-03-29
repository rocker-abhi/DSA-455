"""
    code to reverse the array using the recursion
"""

# # This is the another method to reverse the arr
# def reverse_array(arr):
#     p = 0
#     q = len(arr) - 1 
#     temp = None
#     while p < q :
#         temp = arr[p]
#         arr[p] = arr[q]
#         arr[q] = temp
#         p += 1
#         q -= 1
#     return arr

def reverse_array_recursion(arr,p,q):
    if p > q :
        return arr
    temp = None
    temp = arr[p]
    arr[p] = arr[q]
    arr[q] = temp
    p += 1
    q -= 1
    return reverse_array_recursion(arr,p,q)


if __name__ == "__main__":
    arr = [10,9,8,7,6,5,4,3,2,1]
    p = 0
    q = len(arr)-1
    arr = reverse_array_recursion(arr,p,q)
    print(arr)