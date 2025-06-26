# Optimal - Moore’s Voting Algorithm
# Time: O(n), Space: O(1)

def majority_element_optimal(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Example
print(majority_element_optimal([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
