"""
    largest common prefix .
"""

def largest_common_prefix(arr):
    arr.sort()
    prefix = arr[0]
    
    for string in arr[1:]:
        for i in range(len(prefix)):
            if string[i] != prefix[i]:
                prefix = prefix[:i]
                
    return prefix
    

if __name__ == '__main__':
    arr =  ['abcd', 'abc', 'abcref', 'abcde']
    prefix = largest_common_prefix(arr)
    print(prefix)