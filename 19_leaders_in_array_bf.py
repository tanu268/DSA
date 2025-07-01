# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def find_leaders_brute(nums):
    n = len(nums)
    leaders = []

    for i in range(n):
        is_leader = True
        # Check if any element to the right is greater
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                is_leader = False
                break
        if is_leader:
            leaders.append(nums[i])

    return leaders

# Example
nums = [16, 17, 4, 3, 5, 2]
print("Leaders (Brute Force):", find_leaders_brute(nums))


"""
Real-Life Application
Stock Price Analysis: Identify peak days where a price was higher than all future days.

System Monitoring: Find log entries/events that are greater than all upcoming values."""