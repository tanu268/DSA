# ✅ Problem: Find the largest element in an array.
# 🔢 Input: List of integers
# 🎯 Output: The maximum/largest integer from the list

# ==========================================================
# 🐢 Brute Force Approach - O(n^2)
# ==========================================================
# For each element, check if any other element is greater.
# If not, it's the maximum.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class BruteForceSolution:
    def largestElement(self, nums):
        n = len(nums)
        for i in range(n):
            is_max = True
            for j in range(n):
                if nums[j] > nums[i]:
                    is_max = False
                    break
            if is_max:
                return nums[i]
            
if __name__ == "__main__":
    nums = [10, 25, 3, 67, 42, 88, 5]

    print("Brute Force:", BruteForceSolution().largestElement(nums))