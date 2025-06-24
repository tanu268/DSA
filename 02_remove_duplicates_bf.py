#brute force 
#step 1: Traverse and store unique elements in a new list
#step 2: Copy the result back to the original array(if required)
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)

#copy unique elements back to original list (in place style)
    for i in range(len(result)):
        nums[i] = result[i]
    return len(result)

# Main function to test the brute approach
def main():
    nums = [1, 1, 2, 2, 2]
    length = remove_duplicates(nums)
    print("After removing duplicates (brute):", nums[:length])
    print("Length:", length)

if __name__ == "__main__":
    main()