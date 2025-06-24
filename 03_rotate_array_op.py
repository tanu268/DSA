# Optimal - Use array reversal
# Time: O(n), Space: O(1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(nums, k):
    n = len(nums)
    k = k % n  # Normalize k

    # Step 1: Reverse entire array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(nums, 0, k - 1)

    # Step 3: Reverse the rest
    reverse(nums, k, n-1)

# Example
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums) # Output: [5,6,7,1,2,3,4]
