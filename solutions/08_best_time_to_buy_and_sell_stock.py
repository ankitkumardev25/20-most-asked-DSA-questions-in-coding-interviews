"""
8. Best Time to Buy and Sell Stock
Given an array prices where prices[i] is the price of a given stock on the
i-th day, return the maximum profit you can achieve from this transaction.
You may only buy once and sell once.

Example:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit=5.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit_val = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit_val:
            max_profit_val = price - min_price
    return max_profit_val


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
    print(max_profit([2, 4, 1]))            # 2
