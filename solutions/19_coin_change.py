"""
19. Coin Change (Dynamic Programming)
Given an array of coin denominations and an amount, return the fewest number of
coins needed to make up that amount. Return -1 if it is impossible.

Example:
    Input: coins = [1, 5, 11], amount = 15
    Output: 3  (5 + 5 + 5)

    Input: coins = [2], amount = 3
    Output: -1

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coin_change([1, 5, 11], 15))  # 3
    print(coin_change([1, 2, 5], 11))   # 3
    print(coin_change([2], 3))          # -1
    print(coin_change([1], 0))          # 0
