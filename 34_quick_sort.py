class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot_index - 1)
            self.quickSort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


arr = [1099, 599, 899, 1499, 799]
Solution().quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [599, 799, 899, 1099, 1499]
