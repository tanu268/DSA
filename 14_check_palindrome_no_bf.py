# Brute Force - Convert to string and compare with reversed string
# Time: O(n), Space: O(n)

def is_palindrome_brute(x):
    str_x = str(x)
    return str_x == str_x[::-1]

# Test cases
print(is_palindrome_brute(121))    # True
print(is_palindrome_brute(-121))   # False
print(is_palindrome_brute(10))     # False
