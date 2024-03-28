"""
    Longest Consecutive Sequence in an Array
"""

def consequtive_sequence(arr):
    arr = sorted(arr, reverse=False)
    consecutive_array = [] 
    p = 0 
    q = 1 
    
    while q < len(arr) :
        found_arr = False
        if arr[q] - arr[p] == 1:
            consecutive_array.append(arr[p])
            while q < len(arr) and arr[q]-arr[p] == 1:
                consecutive_array.append(arr[q])
                p += 1
                q += 1
        if found_arr :
            break
        p += 1
        q += 1
        
    return consecutive_array
                

if __name__ == "__main__":
    nums  = [3, 8, 5, 7, 6]
    nums = consequtive_sequence(nums)
    print(nums)