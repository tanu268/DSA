# Brute Force - Use extra list, then copy back
# Time: O(n), Space: O(n)

def remove_element_brute(nums, val):
    result = []

    for num in nums:
        if num != val:
            result.append(num)

    # Copy back to original array
    for i in range(len(result)):
        nums[i] = result[i]

    return len(result)

# Example
nums = [3,2,2,3]
k = remove_element_brute(nums, 3)
print(k, nums[:k])  # Output: 2 [2, 2]
