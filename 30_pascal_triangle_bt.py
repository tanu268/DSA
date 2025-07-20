# Better - Build each row from the previous row
# Time: O(n^2), Space: O(n^2)

def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)  # Start with 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Example
print("Better Pascal Triangle:")
print(generate(5))
