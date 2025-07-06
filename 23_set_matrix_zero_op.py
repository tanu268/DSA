# Optimal Approach (In-place using first row and column as flags)
# Time: O(m × n)
# Space: O(1)

def setZeroesOptimal(matrix):
    m, n = len(matrix), len(matrix[0])
    col0 = 1  # Track whether the first column needs to be zero

    # Step 1: Mark rows and columns in the first row/column
    for i in range(m):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 2: Use markers to set appropriate zeroes
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle the first row
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0

    # Step 4: Handle the first column
    if col0 == 0:
        for i in range(m):
            matrix[i][0] = 0

# Example usage
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

setZeroesOptimal(matrix)
print("Optimal Approach Result:")
for row in matrix:
    print(row)
