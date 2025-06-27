# ==========================================================
# ⚡ Optimal Approach - Manual Traversal - O(n)
# ==========================================================
# Traverse the list once and keep track of the max value.
# Time Complexity: O(n)
# Space Complexity: O(1)

class OptimalSolution:
    def largestElement(self, nums):
        max_element = nums[0]  # Initialize with first element
        for i in range(1, len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
        return max_element
    

if __name__ == "__main__":
    nums = [10, 25, 3, 67, 42, 88, 5]

    print("Optimal (Manual):", OptimalSolution().largestElement(nums))