# Better Approach - Overwrite non-zerovalues, then fill zeros
# Time: O(n), Space: O(1)

def move_zeroes_better(nums):
    index = 0  # index to place the next non-zero

    # First pass: Move all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    # Second pass: Fill the rest with 0s
    for i in range(index, len(nums)):
        nums[i] = 0

# Example
nums = [0, 1, 0, 1, 3, 12]
move_zeroes_better(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]