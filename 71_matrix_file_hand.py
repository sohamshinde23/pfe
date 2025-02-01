import numpy as np

# Create two 3x3 random matrices
matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

# Perform addition
addition_result = np.add(matrix1, matrix2)

# Perform subtraction
subtraction_result = np.subtract(matrix1, matrix2)

# Perform multiplication
multiplication_result = np.dot(matrix1, matrix2)

# Function to display matrix properties
def display_properties(matrix, operation):
    print(f"\n{operation} Result:")
    print(matrix)
    print(f"Shape: {matrix.shape}")
    print(f"Dimensions: {matrix.ndim}")
    print(f"Data Type: {matrix.dtype}")
    print(f"Rank: {np.linalg.matrix_rank(matrix)}")
    print(f"Flattened: {matrix.flatten()}")

# Display properties for each operation
display_properties(addition_result, "Addition")
display_properties(subtraction_result, "Subtraction")
display_properties(multiplication_result, "Multiplication")
