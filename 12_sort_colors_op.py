# Optimal - Dutch National Flag Algorithm
# Time: O(n), Space: O(1)

def sort_colors_optimal(nums):
    low, mid = 0, 0
    high = len(nums) - 1

    # Iterate till mid crosses high
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example
nums = [2,0,2,1,1,0]
sort_colors_optimal(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
