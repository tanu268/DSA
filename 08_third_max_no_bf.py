# Brute Force - Remove duplicates, sort in descending order
# Time: O(n log n), Space: O(n)

def third_max_brute(nums):
    unique = list(set(nums))  # Remove duplicates
    unique.sort(reverse=True)  # Sort descending

    if len(unique) >= 3:
        return unique[2]
    return unique[0]  # Return max if less than 3 unique

# Example
print(third_max_brute([3, 2, 1]))  # Output: 1
print(third_max_brute([1, 2]))     # Output: 2
