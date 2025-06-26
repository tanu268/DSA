# Optimal - Reverse only half of the number
# Time: O(log₁₀n), Space: O(1)

def is_palindrome_optimal(x):
    # Negative numbers are not palindromes
    # Numbers ending with 0 (except 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For even digit count: x == reversed_half
    # For odd digit count: x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Test cases
print(is_palindrome_optimal(121))  # True
print(is_palindrome_optimal(10))   # False
print(is_palindrome_optimal(1221)) # True
