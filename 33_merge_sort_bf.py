# Conceptual Brute Understanding (Simulated)
# Time: O(n log n), Space: O(n)

def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Example of merge only
left = [2, 5, 8]
right = [1, 3, 7]
print("Merged:", merge(left, right))  # [1, 2, 3, 5, 7, 8]
