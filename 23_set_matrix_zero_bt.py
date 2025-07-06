# Better Approach (Using row[] and col[] arrays)
# Time: O(m × n)
# Space: O(m + n)

def setZeroesBetter(matrix):
    m, n = len(matrix), len(matrix[0])
    row = [0] * m
    col = [0] * n

    # Step 1: Mark rows and columns that should be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # Step 2: Set zeroes based on markers
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

# Example usage
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

setZeroesBetter(matrix)
print("Better Approach Result:")
for row in matrix:
    print(row)
