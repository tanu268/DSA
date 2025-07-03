# Optimal In-Place Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def nextPermutationOptimal(nums):
    n = len(nums)

    # Step 1: Find the pivot (first element from end which is smaller than the next one)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap them
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the suffix starting from i + 1
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
nums2 = [1, 2, 3]
nextPermutationOptimal(nums2)
print("Optimal:", nums2)  # Output: [1, 3, 2]
