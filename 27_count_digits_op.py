# Optimal Approach
# Use math.log10 to count digits

# Time Complexity: O(1)
# Space Complexity: O(1)

import math

class Solution:
    def countDigits(self, n):
        return int(math.log10(n)) + 1

# Example
sol = Solution()
print(sol.countDigits(456))  # Output: 3
