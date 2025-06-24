# Optimal - Math formula: sum from 0 to n minus actual sum
# Time: O(n), Space: O(1)

def missing_number_math(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example
print(missing_number_math([3, 0, 1]))  # Output: 2
