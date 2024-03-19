#!/usr/bin/python3
"""main code base"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.
    Args:
    n: The target number of 'H' characters.
    Returns:
    The minimum number of operations needed, or 0 if impossible.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)

    return dp[n]
