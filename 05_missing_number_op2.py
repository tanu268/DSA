# Optimal - XOR approach
# Time: O(n), Space: O(1)

def missing_number_xor(nums):
    xor_all = 0  # XOR of all numbers from 0 to n
    xor_nums = 0  # XOR of all elements in the array
    n = len(nums)

    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i

    # XOR all numbers in the given array
    for num in nums:
        xor_nums ^= num

    # The missing number is the XOR of the two results
    return xor_all ^ xor_nums

# Example
print(missing_number_xor([3, 0, 1]))  # Output: 2
