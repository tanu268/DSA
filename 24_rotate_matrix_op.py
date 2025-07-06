# Optimal Approach (In-place Layer Rotation)
# Time: O(n^2)
# Space: O(1)

def rotateOptimal(matrix):
    n = len(matrix)

    # Rotate layer by layer from outermost to innermost
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save top
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotateOptimal(matrix)
print("Optimal Rotated Matrix:")
for row in matrix:
    print(row)
