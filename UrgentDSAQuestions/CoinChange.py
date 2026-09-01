## Coin Change Problem
## You are given an integer array of coins
## representing coins of different denominations and an integer amount representing a total amount of money.
## Return the fewest number of coins that you need to make up that amount.
## If that amount of money cannot be made up by any combination of the coins, return -1.

##Solution1: Top Down DP Memoization
from ast import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}
        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            min_coins = float('inf')
            for coin in coins:
                diff = amt - coins
                if diff < 0:
                    break
                min_coins = min(min_coins, 1 + min_coins(diff))
            memo[amt] = min_coins
            return min_coins
        res = min_coins(amount)
        if res < float('inf'):
            return res
        return -1
    