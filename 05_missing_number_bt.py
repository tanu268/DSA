# Better - Use set to check membership
# Time: O(n), Space: O(n)

def missing_number_better(nums):
    num_set = set(nums)

    for i in range(len(nums) + 1):
        if i not in num_set:
            return i

# Example
print(missing_number_better([3, 0, 1]))  # Output: 2
