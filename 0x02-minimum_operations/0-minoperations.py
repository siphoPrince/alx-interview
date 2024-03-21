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

    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n] if dp[n] != float('inf') else 0
