#!/usr/bin/python3
"""main code base"""


def makeChange(coins, total):
    """main def file"""
    if total <= 0:
        return 0

    minCoin = [float('inf')] * (total + 1)
    minCoin[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            minCoin[amount] = min(minCoin[amount], minCoin[amount - coin] + 1)

    if minCoin[total] == float('inf'):
        return -1
    else:
        return minCoin[total]
