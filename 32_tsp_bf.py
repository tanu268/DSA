# Brute Force Approach - Check all permutations
# Time: O(n!), Space: O(n)

from itertools import permutations

def tsp_brute(graph):
    n = len(graph)
    min_cost = float('inf')

    for perm in permutations(range(1, n)):
        cost = graph[0][perm[0]]
        for i in range(1, n - 1):
            cost += graph[perm[i - 1]][perm[i]]
        cost += graph[perm[-1]][0]  # return to start

        if cost < min_cost:
            min_cost = cost

    return min_cost

# Example
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Brute Force TSP:", tsp_brute(graph))  # Output: 80
