# Better Approach using prefix min array
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxProfit_better(prices):
    n = len(prices)
    minLeft = [0] * n  # prefix min array
    minLeft[0] = prices[0]

    # Build prefix min array
    for i in range(1, n):
        minLeft[i] = min(minLeft[i-1], prices[i])

    maxProfit = 0
    # Traverse prices and use prefix min to compute max profit
    for i in range(1, n):
        profit = prices[i] - minLeft[i-1]
        maxProfit = max(maxProfit, profit)

    return maxProfit

# Example
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit (Better Approach):", maxProfit_better(prices))
