# Optimal - XOR approach
# Time: O(n), Space: O(1)

def single_number_optimal(nums):
    result = 0

    for num in nums:
        result ^= num  # XOR cancels out duplicate numbers

    return result

# Example
print(single_number_optimal([4,1,2,1,2]))  # Output: 4
