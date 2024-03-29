"""
    fint the union of the two sorted array .
"""

def union_of_two_sorted_array(arr_1, arr_2):
    return arr_1 + arr_2

if __name__ == "__main__":
    arr_1 = [1,2,3,4,5,6,7]
    arr_2 = [8,9,10,11]
    print(f"union by merging the list : {union_of_two_sorted_array(arr_1, arr_2)}" )
    
    # another method is by using the set method to 
    # find the union between the arry
    
    arr_1 = set(arr_1)
    arr_2 = set(arr_2)
    
    arr = arr_1.union(arr_2)
    print(f'union by set method : {arr}')