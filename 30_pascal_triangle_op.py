# Optimal - Generate only a specific row using O(n) space
# Time: O(n * k), Space: O(k)

def generateRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        # Calculate each element using previous element
        row.append(row[-1] * (rowIndex - i + 1) // i)
    return row

# Print all rows using optimal row generator
def generate(numRows):
    result = []
    for i in range(numRows):
        result.append(generateRow(i))
    return result

# Example
print("Optimal Pascal Triangle:")
print(generate(5))
