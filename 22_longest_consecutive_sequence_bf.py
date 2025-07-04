# Brute Force
# Time: O(n^2)
# Space: O(1)

def longestConsecutiveBrute(nums):
    max_len = 0

    for num in nums:
        curr_num = num
        length = 1

        # Check if next elements exist in array
        while curr_num + 1 in nums:
            curr_num += 1
            length += 1

        max_len = max(max_len, length)

    return max_len

# Example
nums = [100, 4, 200, 1, 3, 2]
print("Brute Force:", longestConsecutiveBrute(nums))  # Output: 4

