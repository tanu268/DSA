# Brute Force Approach
# Time: O(min(a, b)), Space: O(1)

def gcd_brute(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

# Example
print("Brute Force GCD of 12 and 18:", gcd_brute(12, 18))  # Output: 6
