# Optimal Approach - Binary Search (Array must be sorted)
# Time: O(log n), Space: O(1)

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Test
arr = [5, 10, 15, 20, 25]
target = 20
print("Index:", binarySearch(arr, target))  # Output: 3
