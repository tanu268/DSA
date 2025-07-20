# Euclidean Algorithm (Iterative)
# Time: O(log(min(a, b))), Space: O(1)

def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
print("Euclidean GCD of 12 and 18:", gcd_euclidean(12, 18))  # Output: 6
