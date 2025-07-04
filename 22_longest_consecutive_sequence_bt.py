# Better Approach
# Time: O(n log n) due to sorting
# Space: O(1) if in-place, else O(n)

def longestConsecutiveBetter(nums):
    if not nums:
        return 0

    nums.sort()
    longest = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Avoid duplicates
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest = max(longest, current_streak)
                current_streak = 1

    return max(longest, current_streak)

# Example
nums = [100, 4, 200, 1, 3, 2]
print("Better Approach:", longestConsecutiveBetter(nums))  # Output: 4
