# Seaching Algorithm: Lineal Search

# Worst case time complexity is O(N)
# Average case time complexity is O(N)
# Best case time complexity is O(1)

arr = [4, 2, 5, 7, 3, 6, 8, 10, 9, 1]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

prompt = int(input("Enter a number between 1 and 10: "))
index = linear_search(arr, prompt)
print(f"{prompt} was found at index: {index}")