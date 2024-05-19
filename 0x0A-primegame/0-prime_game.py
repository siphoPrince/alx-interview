#!/usr/bin/python3
"""main codebase"""


def isWinner(x, nums):
    """main winner function"""
    if not nums or x < 1:
        return None
    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1

    def play_game(n):
        primes = [i for i in range(2, n + 1) if sieve[i]]
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [num for num in primes if num % prime != 0]
            moves += 1
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            moves = play_game(n)
            if moves % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
