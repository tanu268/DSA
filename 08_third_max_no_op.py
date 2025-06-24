# Optimal - Track first, second, third max using variables
# Time: O(n), Space: O(1)

def third_max_optimal(nums):
    first = second = third = float('-inf')

    for num in nums:
        if num in (first, second, third):
            continue
        if num > first:
            first, second, third = num, first, second
        elif num > second:
            second, third = num, second
        elif num > third:
            third = num

    return third if third != float('-inf') else first

# Example
print(third_max_optimal([3, 2, 1]))  # Output: 1
print(third_max_optimal([1, 2]))     # Output: 2
print(third_max_optimal([2, 2, 3, 1])) # Output: 1
