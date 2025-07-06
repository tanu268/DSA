# Brute Force Approach
# Time: O(m × n × (m + n))
# Space: O(1) (not counting placeholder values)

def setZeroesBrute(matrix):
    m, n = len(matrix), len(matrix[0])

    # Step 1: Mark elements as -1 where needed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # Mark the row
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                # Mark the column
                for k in range(m):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1

    # Step 2: Convert all -1s to 0s
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# Example usage
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

setZeroesBrute(matrix)
print("Brute Force Result:")
for row in matrix:
    print(row)
