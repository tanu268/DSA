# Optimal Recursive Merge Sort
# Time: O(n log n), Space: O(n)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # Split array into halves
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return merge(left_half, right_half)

# Helper merge function
def merge(left, right):
    result = []
    i = j = 0

    # Merge sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example
arr = [5, 1, 4, 2, 8]
print("Sorted array:", mergeSort(arr))  # [1, 2, 4, 5, 8]
