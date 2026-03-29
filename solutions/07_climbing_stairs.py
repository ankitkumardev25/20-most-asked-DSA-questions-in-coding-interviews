"""
7. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example:
    Input: n = 3
    Output: 3
    Explanation: 1+1+1, 1+2, 2+1

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n):
    if n <= 2:
        return n
    prev1, prev2 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return prev2


if __name__ == "__main__":
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
    print(climb_stairs(5))  # 8
