# Brute Force - Square then sort the array
# Time: O(n log n), Space: O(n)

def sortedSquares_brute(nums):
    squared = [x * x for x in nums]
    squared.sort()
    return squared

# Example
print(sortedSquares_brute([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
