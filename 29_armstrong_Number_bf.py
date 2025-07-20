"""
armstrong_brute.py
------------------
Brute-force approach to check if a number is an Armstrong number.
Uses string conversion to extract digits.

"""

# Time:  O(d) where d = number of digits
# Space: O(1)

def is_armstrong_brute(n: int) -> bool:
    if n < 0:
        return False

    digits = str(n)
    power = len(digits)
    total = 0

    for ch in digits:
        total += int(ch) ** power

    return total == n


if __name__ == "__main__":
    tests = [153, 370, 9474, 10, 100]
    print("Brute-force Armstrong Check:")
    for num in tests:
        print(f"{num:5} → {is_armstrong_brute(num)}")
