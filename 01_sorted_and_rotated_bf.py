# Brute Force Solution - Check all rotations
# Time: O(n^2), Space: O(n)

def check(nums):
    n = len(nums)

    # Try every possible rotation
    for i in range(n):
        # Rotate the array by i positions
        rotated = nums[i:] + nums[:i]

        # Check if the rotated array is sorted
        if all(rotated[j] <= rotated[j + 1] for j in range(n - 1)):
            return True  # Found a valid sorted rotation

    return False  # No rotation results in a sorted array

# Example Test Cases
print(check([3, 4, 5, 1, 2]))  # True
print(check([1, 2, 3]))        # True
print(check([2, 1, 3, 4]))     # False
