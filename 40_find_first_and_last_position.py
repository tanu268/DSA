"""
Problem 40 - First and Last Position of Element in Sorted Array

🔹 Find the first and last index of a given target in a sorted array.
🔹 If not found, return [-1, -1]
"""

def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid     # store result
                right = mid - 1 # search left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid     # store result
                left = mid + 1  # search right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    return [findFirst(nums, target), findLast(nums, target)]

"""
🔸 Time Complexity: O(log n) - binary search twice
🔸 Space Complexity: O(1) - constant space
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(f"Range for {target1}:", searchRange(nums1, target1))  # Output: [3, 4]

    target2 = 6
    print(f"Range for {target2}:", searchRange(nums1, target2))  # Output: [-1, -1]

    nums2 = [1]
    target3 = 1
    print(f"Range for {target3}:", searchRange(nums2, target3))  # Output: [0, 0]
