
# Time: O(log₁₀n)
# Space: O(1)

def reverseInteger(x):
    INT_MIN = -2**31       # -2147483648
    INT_MAX = 2**31 - 1    # 2147483647

    result = 0
    sign = 1

    # Handle negative number
    if x < 0:
        sign = -1
        x = -x

    while x > 0:
        digit = x % 10
        x = x // 10

        # Check for overflow before pushing digit
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result

# Example usage
print("Reversed 123  →", reverseInteger(123))     # 321
print("Reversed -456 →", reverseInteger(-456))    # -654
print("Overflow Case →", reverseInteger(1534236469))  # 0
