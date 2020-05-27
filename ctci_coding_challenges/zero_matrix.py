"""Write an algorithm such that if an element in an MxN matrix is 0, its entire 
row and column are set to O.

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""

def zero_matrix(matrix):
    
    positions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
          if matrix[row][col] == 0:
              positions.append((row, col))

    for row, col in positions:
        # replace entire row with 0
        matrix[row] = [0] * len(matrix[row])
        # replace col for each row with 0
        for matrix_row in range(len(matrix)):
            matrix[matrix_row][col] = 0
    
    return matrix

print(zero_matrix([[1,1,1],[1,0,1],[1,1,1]]))
print(zero_matrix([[0,1,2,0], [3,4,5,2], [1,3,1,5]]))