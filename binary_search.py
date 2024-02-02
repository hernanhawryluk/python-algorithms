# Seaching Algorithm: Binary Search

# Worst case time complexity is O(N)
# Average case time complexity is O(logN)
# Best case time complexity is O(1)

# Binary search is an efficient algorithm for searching a value in a sorted array.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

prompt = int(input("Enter a number between 1 and 10: "))
index = binary_search(arr, prompt)
print(f"{prompt} was found at index: {index}")