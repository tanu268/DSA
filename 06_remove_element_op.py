# Optimal - Swap with last element when val is found
# Time: O(n), Space: O(1)

def remove_element_optimal(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]  # Replace with last valid element
            n -= 1  # Reduce array size
        else:
            i += 1

    return n  # New length

# Example
nums = [3,2,2,3]
k = remove_element_optimal(nums, 3)
print(k, nums[:k])  # Output: 2 [2, 2]
