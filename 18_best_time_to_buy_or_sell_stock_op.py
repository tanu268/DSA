# Optimal Approach (Single Pass)
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit_optimal(prices):
    minPrice = float('inf')  # track minimum price so far
    maxProfit = 0            # track maximum profit

    for price in prices:
        # update minPrice if current price is smaller
        if price < minPrice:
            minPrice = price
        # update maxProfit if selling at current price gives better profit
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice

    return maxProfit

# Example
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit (Optimal Approach):", maxProfit_optimal(prices))
