"""
    set matrix zero .
"""

def zero_matrix(array):
    n = 0
    
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] == 0 :
                n = j
                array[i] = [0, 0, 0]
                break
    
    for i in range(0, len(array)):
        array[i][n] = 0
    
    return array
                
        
if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(zero_matrix(matrix))