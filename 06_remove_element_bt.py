# Better - Overwrite non-val elements in-place
# Time: O(n), Space: O(1)
# Better - Overwrite non-val elements in-place
# Time: O(n), Space: O(1)

def remove_element_better(nums, val):
    index = 0  # Position to place next valid element

    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1

    return index  # New length

# Example
nums = [3,2,2,3]
k = remove_element_better(nums, 3)
print(k, nums[:k])  # Output: 2 [2, 2]

