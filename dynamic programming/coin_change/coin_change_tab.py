import math
def coin_change(coins, amount):

    tab = [math.inf] * (amount + 1)
    tab[0] = 0
    
    for amount in range(1, amount+1):
        for coin in coins:
            if amount >= coin:
                tab[amount] = min(tab[amount], tab[amount-coin]+ 1)
    

    return tab[-1] if tab[-1] != math.inf else -1


print("Coins = [1, 2, 5] Amount = 11 min number of coins = {}".format(coin_change([1, 2, 5], 11)))
print("Coins = [1, 2, 5] Amount = 100 min number of coins = {}".format(coin_change([1, 2, 5], 100)))
