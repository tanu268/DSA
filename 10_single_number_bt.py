# Better - Use dictionary to count frequency
# Time: O(n), Space: O(n)

def single_number_better(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for num in count:
        if count[num] == 1:
            return num

# Example
print(single_number_better([4,1,2,1,2]))  # Output: 4
