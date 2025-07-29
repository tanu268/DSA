"""
Problem 39 - Search Insert Position

🔹 Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be inserted to keep order.
"""

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    # 🔁 Binary search loop
    while left <= right:
        mid = (left + right) // 2

        # ✅ Target found at mid
        if nums[mid] == target:
            return mid

        # 🔼 Target is larger, search right half
        elif nums[mid] < target:
            left = mid + 1

        # 🔽 Target is smaller, search left half
        else:
            right = mid - 1

    # ⛔ Target not found: left is insertion point
    return left

"""
🔸 Time Complexity: O(log n) - binary search
🔸 Space Complexity: O(1) - constant space
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"Insert position of {target1}:", searchInsert(nums1, target1))  # Output: 2

    target2 = 2
    print(f"Insert position of {target2}:", searchInsert(nums1, target2))  # Output: 1

    target3 = 7
    print(f"Insert position of {target3}:", searchInsert(nums1, target3))  # Output: 4

    target4 = 0
    print(f"Insert position of {target4}:", searchInsert(nums1, target4))  # Output: 0
