# Brute Force Approach
# Time Complexity: O((n + m) * log(n + m))
# Space Complexity: O(n + m)
def union_brute(nums1, nums2):
    # Combine both arrays
    combined = nums1 + nums2
    # Use set to eliminate duplicates
    union_set = set(combined)
    # Convert set to sorted list
    return sorted(list(union_set))

# Example usage
nums1 = [1, 2, 2, 3]
nums2 = [2, 3, 4, 5]
print("Union (Brute Force):", union_brute(nums1, nums2))



