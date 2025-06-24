# Optimal - Two pointers from ends, fill result from back
# Time: O(n), Space: O(n)

def sortedSquares_optimal(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Start filling from the end

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1

    return result

# Example
print(sortedSquares_optimal([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
