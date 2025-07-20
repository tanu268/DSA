# Optimal Approach - DP with Bitmasking
# Time: O(n^2 * 2^n), Space: O(n * 2^n)

def tsp_dp(graph):
    n = len(graph)
    dp = [[-1] * (1 << n) for _ in range(n)]

    def visit(city, mask):
        if mask == (1 << n) - 1:
            return graph[city][0]  # return to start

        if dp[city][mask] != -1:
            return dp[city][mask]

        min_cost = float('inf')
        for next_city in range(n):
            if not (mask & (1 << next_city)):
                cost = graph[city][next_city] + visit(next_city, mask | (1 << next_city))
                min_cost = min(min_cost, cost)

        dp[city][mask] = min_cost
        return min_cost

    return visit(0, 1)  # start at city 0 with mask 1 (only city 0 visited)

# Example
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("DP TSP:", tsp_dp(graph))  # Output: 80
