# Better Approach
# Divide the number by 10 until it becomes 0

# Time Complexity: O(log₁₀n)
# Space Complexity: O(1)

class Solution:
    def countDigits(self, n):
        count = 0
        while n > 0:
            n //= 10
            count += 1
        return count

# Example
sol = Solution()
print(sol.countDigits(456))  # Output: 3
