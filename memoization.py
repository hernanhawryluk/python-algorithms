# Memoization: Applied to Fibonacci

# Worst case time complexity is O(n)
# Average case time complexity is O(n) <- Improved by memoization
# Best case time complexity is O(1)    <- When previously calculated

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

while True:
    n = input("Ingresa un número: ")
    if n.isdigit() == False:
        break
    n = int(n)
    result = fibonacci(n)
    print(f"El número Fibonacci en la posición {n} es: {result}")