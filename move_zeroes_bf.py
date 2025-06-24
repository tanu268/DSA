# Brute Force Approach
# 1. Traverse and collect all non-zero elements in a new list
# 2. Count number of zeros
# 3. Append that many zeros at the end
# 4. Copy back to original array

def move_zeroes_brute(nums):
    result = []
    count_zeros = 0

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            count_zeros += 1

    result += [0] * count_zeros  # Append required zeros

    # Copy result back to original array
    for i in range(len(nums)):
        nums[i] = result[i]

# Main function for brute
def main():
    nums = [0, 1, 0, 3, 12]
    temp = nums[:]  # create a copy to test
    move_zeroes_brute(temp)
    print("After moving zeroes (brute):", temp)

if __name__ == "__main__":
    main()
