# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n) to store leaders (can be reduced to O(1) if printing directly)
class Solution:
    def leaders(self, nums):
        leaders = []  # To store leader elements
        max_so_far = float('-inf')  # Initialize with smallest possible value

        # Traverse from right to left
        for num in reversed(nums):
            # If current number is greater than max_so_far, it's a leader
            if num > max_so_far:
                leaders.append(num)
                max_so_far = num

        # Reverse to maintain original order
        return leaders[::-1]

# Example usage
nums = [16, 17, 4, 3, 5, 2]
sol = Solution()
print("Leaders (Optimal):", sol.leaders(nums))
