# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n) for two separate lists
def rearrange_brute(nums):
    positives = []
    negatives = []

    # Separate positive and negative numbers
    for num in nums:
        if num > 0:
            positives.append(num)
        else:
            negatives.append(num)

    result = []

    # Alternate between positives and negatives
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])

    return result

# Example
nums = [3, 1, -2, -5, 2, -4]
print("Brute Force:", rearrange_brute(nums))


"""

----------------------------------------------------
📌 Real-World Applications:

1. Signal Processing:
   - Used in digital signal transformation where alternating values represent wave fluctuations.

2. Financial Data Normalization:
   - Alternating profit/loss sequences help in simplifying financial trends.

3. Data Visualization:
   - Alternating signs can be used in bar graphs to represent deviation above/below a baseline.

4. Load Balancing:
   - In scheduling systems, alternating light and heavy tasks ensures even distribution of load.

5. Event Simulation:
   - Useful in systems like games or models where actions alternate in type (e.g., attack/defend).

----------------------------------------------------
📚 Algorithmic Concepts Practiced:

- Two-pointer technique with index tracking.
- Preserving relative order while applying constraints.
- Greedy placement without backtracking.

"""
