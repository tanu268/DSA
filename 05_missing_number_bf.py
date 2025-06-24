# Brute Force - Sort and check missing number
# Time: O(n log n), Space: O(1)

def missing_number_brute(nums):
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)  # If all numbers are in place

# Example
print(missing_number_brute([3, 0, 1]))  # Output: 2
