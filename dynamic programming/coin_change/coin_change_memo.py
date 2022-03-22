import math
def coin_change(coins, amount):
    
    memo = {0 : 0}
    def get_min(amount):
        if amount in memo:
            return memo[amount]
        curr = math.inf
        for coin in coins:
            if amount >= coin:
               curr = min(curr,  get_min(amount-coin) + 1)
        memo[amount] = curr
        return curr



    ans = get_min(amount)
    return ans if ans != math.inf else -1


print("Coins = [1, 2, 5] Amount = 11 min number of coins = {}".format(coin_change([1, 2, 5], 11)))
print("Coins = [1, 2, 5] Amount = 100 min number of coins = {}".format(coin_change([1, 2, 5], 100)))
