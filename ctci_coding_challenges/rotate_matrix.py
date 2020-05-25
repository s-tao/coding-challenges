"""Rotate Matrix: Given an image represented by an NxN matrix, where each pixel 
in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
Can you do this in place?
"""

def rotate_matrix(matrix):

    rows = len(matrix) - 1
    cols = len(matrix[0]) 

    # swap rows first
    for row in range(len(matrix)//2):
        matrix[row], matrix[rows] = matrix[rows], matrix[row]
        rows -= 1
    
    # swap indices
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if col == row or col < row:
                continue
            
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    print(matrix)

rotate_matrix([[1,2,3], [4,5,6], [7,8,9]])
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

rotate_matrix([[5,1,9,11], [2,4,8,10], [13,3,6,7], [15,14,12,16]])
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
