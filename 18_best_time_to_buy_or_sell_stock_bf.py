# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def maxProfit_brute(prices):
    maxProfit = 0
    n = len(prices)

    # Try every pair (i, j) where i < j
    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit

# Example
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit (Brute Force):", maxProfit_brute(prices))


"""
📌 Real-Life Application:
Stock market price analysis

Dynamic price optimization in e-commerce

Finding max profit opportunity in time series

📌 Algorithmic Use-Case:
Sliding window style optimization

Greedy strategy

"""