# Optimal Solution
# Time: O(n), Space: O(n)

def twoSum(nums,target):
    #Stores number as key and its index as value
    hashmap = {}

    for i,num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[num] = i

# Example
print(twoSum([2,7,11,15],9)) #output: [0,1]