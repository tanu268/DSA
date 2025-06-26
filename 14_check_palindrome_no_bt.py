# Better - Convert to string, reverse manually using loop
# Time: O(n), Space: O(n)

def is_palindrome_better(x):
    if x < 0:
        return False
    str_x = str(x)
    reversed_str = ""
    for ch in str_x:
        reversed_str = ch + reversed_str  # reverse string manually
    return str_x == reversed_str

# Test cases
print(is_palindrome_better(121))   # True
print(is_palindrome_better(123))   # False
