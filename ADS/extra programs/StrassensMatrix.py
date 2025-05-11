import numpy as np

def strassen_matrix_multiplication(A, B):
    """Multiply two square matrices using Strassen's algorithm."""
    n = A.shape[0]
    
    if n == 1:
        return A * B

    # Splitting matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Compute the 7 Strassen sub-matrices
    M1 = strassen_matrix_multiplication(A11 + A22, B11 + B22)
    M2 = strassen_matrix_multiplication(A21 + A22, B11)
    M3 = strassen_matrix_multiplication(A11, B12 - B22)
    M4 = strassen_matrix_multiplication(A22, B21 - B11)
    M5 = strassen_matrix_multiplication(A11 + A12, B22)
    M6 = strassen_matrix_multiplication(A21 - A11, B11 + B12)
    M7 = strassen_matrix_multiplication(A12 - A22, B21 + B22)

    # Compute final quadrants of the result matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine quadrants into final matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = strassen_matrix_multiplication(A, B)
print("Resultant Matrix:")
print(result)
