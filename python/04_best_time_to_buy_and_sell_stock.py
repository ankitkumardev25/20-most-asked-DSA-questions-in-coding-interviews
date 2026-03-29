"""
Q4. Best Time to Buy and Sell Stock (Category: Arrays)

Problem: Given daily stock prices, find the maximum profit achievable
         from one buy-sell transaction.

Approach: Track the minimum price seen so far. For each day, compute
          the potential profit and update the global maximum.

Time Complexity : O(n)
Space Complexity: O(1)
"""


def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit_val = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit_val = max(max_profit_val, price - min_price)
    return max_profit_val


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0  (no profit possible)
