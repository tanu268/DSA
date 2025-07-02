# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(n) for result only
def rearrange_better(nums):
    result = [0] * len(nums)  # Final output array
    pos_index = 0
    neg_index = 1

    for num in nums:
        if num > 0:
            result[pos_index] = num
            pos_index += 2
        else:
            result[neg_index] = num
            neg_index += 2

    return result

# Example
nums = [3, 1, -2, -5, 2, -4]
print("Better Approach:", rearrange_better(nums))
