# Euclidean Algorithm (Recursive)
# Time: O(log(min(a, b))), Space: O(log(min(a, b))) due to recursion stack

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Example
print("Recursive GCD of 12 and 18:", gcd_recursive(12, 18))  # Output: 6
