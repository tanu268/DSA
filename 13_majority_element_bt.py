# Better Approach - Use dictionary to count frequencies
# Time: O(n), Space: O(n)

def majority_element_better(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num

# Example
print(majority_element_better([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
