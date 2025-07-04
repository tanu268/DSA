# Optimal Approach using HashSet
# Time: O(n)
# Space: O(n)

def longestConsecutiveOptimal(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only try to build a sequence from numbers that are the start
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Expand the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

# Example
nums = [100, 4, 200, 1, 3, 2]
print("Optimal Approach:", longestConsecutiveOptimal(nums))  # Output: 4
