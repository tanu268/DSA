"""
🔹 Problem 153 - Find Minimum in Rotated Sorted Array

🔸 Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the rotated sorted array `nums` (with **no duplicate** elements), return the minimum element.

Example:
Input: nums = [3,4,5,1,2]
Output: 1

Explanation:
Original sorted array [1,2,3,4,5] was rotated. The smallest element is 1.

🔸 Constraints:
- n == len(nums)
- 1 <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
- All the integers of nums are unique.
- nums is guaranteed to be a rotated sorted array.

🔸 Complexity:
- Time: O(log n) using binary search.
- Space: O(1)
"""

def findMin(nums: list[int]) -> int:
    """
    Uses binary search to find the minimum in a rotated sorted array without duplicates.
    """
    left, right = 0, len(nums) - 1

    # If the array is not rotated (already sorted), the first element is minimum
    if nums[left] <= nums[right]:
        return nums[left]

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the rightmost, minimum is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is at mid or in left half
            right = mid

    return nums[left]


# 🔹 Example Use Case
if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))  # Expected: 1
    print(findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0
    print(findMin([1]))  # Expected: 1
    print(findMin([2, 1]))  # Expected: 1
