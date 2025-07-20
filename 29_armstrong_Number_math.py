"""
armstrong_math.py
-----------------
Math-based approach to check if a number is an Armstrong number.
Avoids string conversion and uses only integer operations.

"""

# Time:  O(d) where d = number of digits
# Space: O(1)

def is_armstrong_math(n: int) -> bool:
    if n < 0:
        return False

    if n == 0:
        return True

    temp = n
    digits = 0
    while temp:
        digits += 1
        temp //= 10

    power = digits
    total = 0
    temp = n

    while temp:
        digit = temp % 10
        total += pow(digit, power)
        temp //= 10

    return total == n


if __name__ == "__main__":
    tests = [153, 370, 9474, 10, 100]
    print("Math-based Armstrong Check:")
    for num in tests:
        print(f"{num:5} → {is_armstrong_math(num)}")
