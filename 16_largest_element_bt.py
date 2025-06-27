# ==========================================================
# 🛠 Better Approach - Using built-in max() function - O(n)
# ==========================================================
# This approach uses Python’s built-in max() function,
# which internally performs a linear scan.
# Time Complexity: O(n)
# Space Complexity: O(1)

class BetterSolution:
    def largestElement(self, nums):
        return max(nums)
    
if __name__ == "__main__":
    nums = [10, 25, 3, 67, 42, 88, 5]

    print("Better (Built-in max):", BetterSolution().largestElement(nums))