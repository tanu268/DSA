# Better Approach - Use prefix sums to calculate subarray sums
# Time: O(n²), Space: O(n)

def max_subarray_better(nums):
    n = len(nums)
    prefix = [0] * (n+1)

    # Create prefix sum array
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    max_sum = float('-inf')
    for i in range(n):
        for j in range(i+1, n+1):
            subarray_sum = prefix[j] - prefix[i]
            max_sum = max(max_sum, subarray_sum)

    return max_sum

# Example
print(max_subarray_better([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
