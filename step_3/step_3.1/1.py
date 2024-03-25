"""
    Find the largest element in the array .

"""

def largest_number(arr):

    max = arr[0]
    for i in arr:
        if i > max :
            max = i
    return max

if __name__ == "__main__":
    size_of_arr = int(input("please enter the size of the array : "))
    arr = []
    for i in range(size_of_arr):
        arr.append(int(input("enter the item in the array : ")))
    
    max = largest_number(arr)
    print(f"max number in the array is : {max}")