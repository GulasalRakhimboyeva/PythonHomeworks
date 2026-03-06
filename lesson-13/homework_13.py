import numpy as np
# # 1. Create a vector with values ranging from 10 to 49.
# vector=np.arange(10, 50)
# print(vector)

# # 2. Create a 3x3 matrix with values ranging from 0 to 8.
# matrix=np.arange(0, 9).reshape(3,3)
# print(matrix)

# # 3. Create a 3x3 identity matrix.
# i_matrix=np.eye(3)
# print(i_matrix)

# # 4. Create a 3x3x3 array with random values.
# random_m=np.random.randint(1, 55, (3, 3, 3))
# print(random_m)

# # 5. Create a 10x10 array with random values and find the minimum and maximum values.
# random_arr=np.random.rand(10,10)
# print(f'minimum {random_arr.min()}, \nmaximum{random_arr.max()}')

# # 6. Create a random vector of size 30 and find the mean value.
# random_vec=np.random.randint(1,31, ( 30,))
# print(random_vec)
# print(f'mean is {random_vec.mean()}')

# # 7. Normalize a 5x5 random matrix.
# matrix=np.random.randint(1,40, (5, 5))
# n_matrix=(matrix-matrix.min())/(matrix.max()-matrix.min())
# print(n_matrix)

# # 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
# matrix1=np.random.randint(1,40, (5, 3))
# matrix2=np.random.randint(1,40, (3, 2))
# mul_matrix=matrix1@matrix2
# print(mul_matrix)

# # 9. Create two 3x3 matrices and compute their dot product.  
# matrix1=np.random.randint(1,40, (3, 3))
# matrix2=np.random.randint(1,40, (3, 3))
# dot_product=matrix1.dot(matrix2)
# print(dot_product)

# # 10. Given a 4x4 matrix, find its transpose.
# matrix1=np.random.randint(1,40, (4, 4))
# matrix_t=np.transpose(matrix1)
# print(matrix1, matrix_t)

# # 11. Create a 3x3 matrix and calculate its determinant.  
# matrix1=np.random.randint(1,40, (3, 3))
# det=np.linalg.det(matrix1)
# print(det)

# # 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \). 
# A=np.random.randint(1,30, (3,4))
# B=np.random.randint(1,30, (4,3))
# mult=A.dot(B)
# print(mult)

# # 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
# matrix=np.random.randint(1, 20, (3,3))
# vector=np.random.randint(1, 20, (3, 1))
# result = matrix @ vector 
# print(result)

# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector. 
A=np.random.randint(1, 20, (3,3))
b=np.random.randint(1, 20, (3, 1))
x=np.linalg.solve(A,b)
print(x)
# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
A=np.random.randint(1, 20, (5,5))
row_sums=A.sum(axis=1)
column_sums=A.sum(axis=0)

