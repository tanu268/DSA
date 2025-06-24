# Better - Track top 3 manually using a list
# Time: O(n), Space: O(1) assuming fixed max 3 values

def third_max_better(nums):
    top = []

    for num in nums:
        if num not in top:
            top.append(num)
            top.sort(reverse=True)
            if len(top) > 3:
                top.pop()

    return top[2] if len(top) == 3 else top[0]

# Example
print(third_max_better([3, 2, 1]))  # Output: 1
print(third_max_better([1, 2]))     # Output: 2
