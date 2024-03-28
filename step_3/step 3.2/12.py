"""
    rotate matrix by 90*
    
    [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate_by_90(array):
    new_list = []
    
    for i in range(0, len(array)):
        row_data = []
        for j in range(len(array)-1, -1, -1):
            item = array[j][i]
            row_data.append(item)
        new_list.append(row_data)
    return new_list   
            
if __name__ == "__main__":
    array = [[1,2,3],[4,5,6],[7,8,9]]
    array = rotate_by_90(array)
    print(array)