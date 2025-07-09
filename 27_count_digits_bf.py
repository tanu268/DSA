# Brute Force Approach
# Convert the number to string and count its length

# Time Complexity: O(log₁₀n)
# Space Complexity: O(log₁₀n) — because str(n) uses memory

class Solution:
    def countDigits(self, n):
        return len(str(n))

# Example
sol = Solution()
print(sol.countDigits(456))  # Output: 3
