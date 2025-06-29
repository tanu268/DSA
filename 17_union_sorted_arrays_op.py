# Optimal Approach (Two Pointers without Set)
# Time Complexity: O(n + m)
# Space Complexity: O(1) [excluding output list]
def union_optimal(nums1, nums2):
    i, j = 0, 0
    result = []

    # Traverse both arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
        else:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < len(nums1):
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < len(nums2):
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    return result

# Example usage
nums1 = [1, 2, 2, 3]
nums2 = [2, 3, 4, 5]
print("Union (Optimal Approach):", union_optimal(nums1, nums2))


'''
Algorithmic Use Case
Uses two-pointer technique

Demonstrates set operations

Related to merge step in merge sort
'''
