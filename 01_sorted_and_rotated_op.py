# Optimal Solution - Count number of drops
# TC O(n)
def check(nums):
    count = 0  # Count how many times nums[i] > nums[i+1]
    n = len(nums)

    for i in range(n):
        # Wrap around using modulo to include last and first element
        if nums[i] > nums[(i + 1) % n]:
            count += 1
            if count > 1:
                return False  # More than one drop → not sorted & rotated

    return True  # Valid sorted & rotated array

# Example
print(check([3, 4, 5, 1, 2]))  # True
print(check([1, 2, 3]))        # True
print(check([2, 1, 3, 4]))     # False


'''QUICK TIP
The modulus operator is super useful when you're working with cyclic or circular data—like wrapping around an array or keeping time on a 12-hour clock.'''