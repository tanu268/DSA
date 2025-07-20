# Brute Force - Using formula: nCr = n! / (r! * (n-r)!)
# Time: O(n^2 * r), Space: O(1) ignoring output list

import math

def generate(numRows):
    result = []
    for n in range(numRows):
        row = []
        for r in range(n + 1):
            val = math.comb(n, r)  # You can also use math.factorial manually
            row.append(val)
        result.append(row)
    return result

# Example
print("Brute Force Pascal Triangle:")
print(generate(5))
