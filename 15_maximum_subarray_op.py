# Optimal - Kadane’s Algorithm
# Time: O(n), Space: O(1)

def max_subarray_optimal(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # Extend the current subarray or start new from current number
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)  # Update global max if needed

    return max_sum

# Example
print(max_subarray_optimal([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
