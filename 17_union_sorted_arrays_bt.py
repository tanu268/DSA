# Better Approach (Two Pointers + Set)
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def union_better(nums1, nums2):
    i, j = 0, 0
    result_set = set()

    # Traverse both arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result_set.add(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            result_set.add(nums2[j])
            j += 1
        else:
            result_set.add(nums1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < len(nums1):
        result_set.add(nums1[i])
        i += 1

    while j < len(nums2):
        result_set.add(nums2[j])
        j += 1

    return sorted(list(result_set))

# Example usage
nums1 = [1, 2, 2, 3]
nums2 = [2, 3, 4, 5]
print("Union (Better Approach):", union_better(nums1, nums2))
