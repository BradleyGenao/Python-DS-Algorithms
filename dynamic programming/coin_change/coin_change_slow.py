import math
def coin_change(coins, amount):
    
    def get_min(amount):
        if amount == 0:
            return 0
        curr = math.inf
        for coin in coins:
            if amount >= coin:
               curr = min(curr,  get_min(amount-coin) + 1)
        return curr



    ans = get_min(amount)
    return ans if ans != math.inf else -1


print("Coins = [1, 2, 5] Amount = 11 min number of coins = {}".format(coin_change([1, 2, 5], 11)))
print("Coins = [1, 2, 5] Amount = 100 min number of coins = TLE")
