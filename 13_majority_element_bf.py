# Brute Force - Count each element's frequency manually
# Time: O(n²), Space: O(1)

def majority_element_brute(nums):
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n // 2:
            return nums[i]

# Example
print(majority_element_brute([2, 2, 1, 1, 1, 2, 2]))  # Output: 2