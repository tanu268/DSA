# Brute Force Approach
# Time Complexity: O(n! · n log n)
# Space Complexity: O(n!)

from itertools import permutations

def nextPermutationBrute(nums):
    # Generate all permutations and sort them
    perms = sorted(set(permutations(nums)))

    # Find the current permutation's index
    for i in range(len(perms)):
        if list(perms[i]) == nums:
            # Return the next permutation if exists, else the first one
            return list(perms[(i + 1) % len(perms)])

# Example usage
nums = [1, 2, 3]
result = nextPermutationBrute(nums)
print("Brute Force:", result)  # Output: [1, 3, 2]



"""
Real-Life Applications:

Generating Combinations for Test Cases:

Efficient way to move through permutations without listing all of them.

Lexicographical Order Processing:

Useful in string processing and dictionary ordering problems.

Password/Token Generators:

Helps generate the next valid combination.

AI Simulations and Pathfinding:

Used to explore next moves or strategies in lexicographical order.



Algorithmic Concepts Practiced:

Two-pointer reverse and swap

Greedy in-place transformations

Understanding permutation sequence transitions


"""