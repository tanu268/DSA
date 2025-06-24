# Brute Force - Rotate array one step at a time, k times
# Time: O(n * k), Space: O(1)

def rotate(nums,k):
    n = len(nums)
    k = k % n  # In case K > n

    for _ in range(k):
        last = nums[-1]  # Store last element
        #Shift all elements to the right
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last # Place last at the start


# Example
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)  #Output: [5,6,7,1,2,3,4]