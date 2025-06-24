# Better - Use an extra array to store rotated result
# Time: O(n), Space: O(n)

def rotate(nums, k):
    n = len(nums)
    k = k % n # Normalize k
    result = [0] * n # Extra space to hold rotated values


    for i in range(n):
        result[(i + k) % n] = nums[i]


    #Copy back to original array
    for i in range(n):
        nums[i] = result[i]

# Example
nums = [1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)  # Output: [5,6,7,1,2,3,4]