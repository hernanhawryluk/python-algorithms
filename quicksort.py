# Sorting Algorithm: Quick Sort

# Worst case time complexity is O(N^2)
# Average case time complexity is O(NlogN)
# Best case time complexity is O(NlogN)

n = [4, 2, 5, 7, 3, 6, 8, 10, 9, 1]

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

sorted_n = quicksort(n)
print(sorted_n)
