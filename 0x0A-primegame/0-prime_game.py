#!/usr/bin/python3
"""using  prime generator"""


def generate_primes(n):
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    for i in range(int(n**0.5)+1, n+1):
        if sieve[i]:
            primes.append(i)
    return primes


def isWinner(x, nums):
    def can_win(n, primes):
        if n <= 1:
            return False
        if n in primes:
            return True
        return len([p for p in primes if n % p == 0]) % 2 == 0

    primes = generate_primes(max(max(nums), 10))
    maria_wins = 0
    for n in nums:
        if can_win(n, primes):
            maria_wins += 1

    if maria_wins > x - maria_wins:
        return "Maria"
    elif maria_wins < x - maria_wins:
        return "Ben"
    else:
        return None