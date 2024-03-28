"""
    Leaders in a array .
"""

def find_leaders(arr):
    leaders_list = []
    
    for i in range(0, len(arr)):
        found_greater = False
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                found_greater = True
        if found_greater == False:
            if arr[i] not in leaders_list:
                leaders_list.append(arr[i])
    
    return leaders_list

if __name__ == "__main__":
    arr = [10, 22, 12, 3, 0, 6]
    arr = find_leaders(arr)
    print(arr)