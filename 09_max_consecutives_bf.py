# Brute Force
# Traverse and count 1s manually
# Reset counter when 0 is found

def max_consecutive_ones_brute(nums):
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count = 0
            j = i
            while j < len(nums) and nums[j] == 1:
                count += 1
                j += 1
            max_count = max(max_count, count)
    return max_count

# Main function for brute
def main():
    nums = [1, 1, 0, 1, 1, 1]
    result = max_consecutive_ones_brute(nums)
    print("Max consecutive 1s (brute):", result)

if __name__ == "__main__":
    main()
