"""
    two sum problem
"""

def two_sum(array, target):
    result = [-1,-1]
    found_target = False
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if i == j:
                continue
            else:
                if array[i] + array[j] == target:
                    result[0] = i
                    result[1] = j
                    found_target = True
                    break
            if found_target :
                break

    return found_target, result

if __name__ == "__main__":
    size = int(input("Please enter the size of the array : "))
    arr = []
    
    for i in range(0,size):
        element = int(input("please enter the item : "))
        arr.append(element)
        
    target = int(input("please enter the target sum :"))
    found_target, result = two_sum(arr, target)
    if found_target :
        print(f'result found : {result}')
    else:
        print(f'result not found : {result}')