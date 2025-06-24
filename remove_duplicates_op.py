# Optimal Approach 
# Use two pointers:
# i - points to last unique value
# j - scans through the list

def remove_duplicates(nums):
    if not nums:
     return 0
    
    i = 0 # Slow pointer 
    for j in range(1,len(nums)):
       if nums[j] !=  nums[i]:
          i += 1
          nums[i] = nums[j]

    return i + 1 #because index starts at 0


# Main function to test the optimal approach
def main():
    nums = [1, 1, 2, 2, 3]
    length = remove_duplicates(nums)
    print("After removing duplicates (optimal):", nums[:length])
    print("Length:", length)

if __name__ == "__main__":
    main()