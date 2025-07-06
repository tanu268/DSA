# Better Approach (Transpose + Reverse)
# Time: O(n^2)
# Space: O(1)

def rotateBetter(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotateBetter(matrix)
print("Better (Transpose + Reverse) Rotated Matrix:")
for row in matrix:
    print(row)
