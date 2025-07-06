# Brute Force Approach
# Time: O(n^2)
# Space: O(n^2)

def rotateBrute(matrix):
    n = len(matrix)
    # Step 1: Create a new matrix of the same size
    rotated = [[0] * n for _ in range(n)]

    # Step 2: Fill rotated matrix using the formula
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    # Step 3: Copy rotated matrix back to the original
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated[i][j]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotateBrute(matrix)
print("Brute Force Rotated Matrix:")
for row in matrix:
    print(row)
