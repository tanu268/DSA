# Brute Force - Try every possible subarray and calculate the sum
# Time: O(n²), Space: O(1)

def max_subarray_brute(nums):
    max_sum = float('-inf')
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]           # Add next element
            max_sum = max(max_sum, current_sum)  # Update max sum if needed

    return max_sum

# Example
print(max_subarray_brute([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
