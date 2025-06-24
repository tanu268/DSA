# Optimal Approach (Two Pointers)
# i points to the position where next non-zero should be placed
# j traverses the array

def move_zeroes_optimal(nums):
    i = 0  # index for next non-zero

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]  # swap
            i += 1  # move i to next available spot

# Main function for optimal
def main():
    nums = [0, 1, 0, 3, 12]
    temp = nums[:]
    move_zeroes_optimal(temp)
    print("After moving zeroes (optimal):", temp)

if __name__ == "__main__":
    main()
