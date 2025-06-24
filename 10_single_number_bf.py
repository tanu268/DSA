# Brute Force - Check frequency of each element manually
# Time: O(n²), Space: O(1)

def single_number_brute(nums):
    for i in range(len(nums)):
        found = False
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                found = True
                break
        if not found:
            return nums[i]

# Example
print(single_number_brute([4,1,2,1,2]))  # Output: 4
