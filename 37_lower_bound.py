# Time Complexity: O(log n)
# Space Complexity: O(1)

def lower_bound(arr, x):
    low = 0
    high = len(arr)
    ans = len(arr)  # Default: if x is greater than all elements

    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid
        else:
            low = mid + 1

    return ans

# Example
arr = [1, 2, 4, 4, 5, 6, 8]
x = 4
index = lower_bound(arr, x)
print(f"Lower Bound of {x} is at index: {index}")  # Output: 2
