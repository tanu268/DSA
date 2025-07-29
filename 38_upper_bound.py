# Time Complexity: O(log n)
# Space Complexity: O(1)

def upper_bound(arr, x):
    low = 0
    high = len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1
           

    return low
           

# Example
arr = [1, 2, 4, 4, 5, 6, 8]
x = 5
index = upper_bound(arr, x)
print(f"upper Bound of {x} is at index: {index}")  # Output: 2
