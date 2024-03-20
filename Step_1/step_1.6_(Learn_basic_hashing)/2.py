"""
    Count frequency of each element in the array
    note : instead of anything we use dictinory in python code .
    
    
    
    Example 1:
        Input: arr[] = {10,5,10,15,10,5};
        Output: 10  3
                5   2
                15  1
        Explanation: 10 occurs 3 times in the array
                5 occurs 2 times in the array
                    15 occurs 1 time in the array

        Example2: 
        Input: arr[] = {2,2,3,4,4,2};
        Output: 2  3
                3  1
                4  2
        Explanation: 2 occurs 3 times in the array
                3 occurs 1 time in the array
                    4 occurs 2 time in the array
"""

def find_count(arr):
        count_of_repeat_character = {}
        character_to_count = []
        
        # this for loop is used to find that need to count
        for i in range(len(arr)-1):
                if arr[i] not in character_to_count:
                        character_to_count.append(arr[i])
                
        # this loop is used to find the count 
        for i in range(len(character_to_count)):
                count = 0
                for j in range(len(arr)-1):
                        if character_to_count[i] == arr[j]:
                                count += 1
                count_of_repeat_character[i] = count
        
        return count_of_repeat_character
        
arr = [2,2,3,4,4,2]
count = find_count(arr)
for key, value in count.items():
        print(f'{key} : {value}')


