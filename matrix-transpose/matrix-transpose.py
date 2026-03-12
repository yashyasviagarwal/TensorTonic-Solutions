import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows, cols = len(A), len(A[0])
    result = np.empty((cols, rows))
    for i in range(rows):
        for j in range(cols):
            result[j, i] = A[i][j]  
    return result
