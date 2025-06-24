# Optimal Approach
# Count current streak of 1s while iterating
# Update max streak whenever 0 appears

def max_consecutive_ones_optimal(nums):
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

# Main function for optimal
def main():
    nums = [1, 1, 0, 1, 1, 1]
    result = max_consecutive_ones_optimal(nums)
    print("Max consecutive 1s (optimal):", result)

if __name__ == "__main__":
    main()
