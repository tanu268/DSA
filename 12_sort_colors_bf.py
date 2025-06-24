# Brute Force - Count and overwrite
# Time: O(n), Space: O(1)

def sort_colors_brute(nums):
    count = [0, 0, 0]  # count of 0s, 1s, and 2s

    for num in nums:
        count[num] += 1

    # Overwrite original array based on count
    i = 0
    for color in range(3):  # 0, 1, 2
        for _ in range(count[color]):
            nums[i] = color
            i += 1

# Example
nums = [2,0,2,1,1,0]
sort_colors_brute(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
