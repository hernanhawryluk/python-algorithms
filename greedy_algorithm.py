# Greedy Algorithm: Coin Change

# Time complexity is O(N), where N is the number of coins
# Space complexity is O(1) as the result is stored in a list

def greedy_coin_change(amount, coins):
    coins.sort(reverse=True)
    change = []

    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin

    return change

total_amount = 63
available_coins = [25, 10, 5, 1]

change_result = greedy_coin_change(total_amount, available_coins)

print(f"El cambio para {total_amount} utilizando monedas {available_coins} es:")
print(change_result)