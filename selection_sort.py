# Sorting Algorithm: Selection Sort

# Worst case time complexity is O(N^2)
# Average case time complexity is O(N^2)
# Best case time complexity is O(N^2)

arr = [4, 2, 5, 7, 3, 6, 8, 10, 9, 1]

for i in range(len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)