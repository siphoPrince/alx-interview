#!/usr/bin/python3
"""using  prime generator"""
def generate_primes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(limit + 1) if primes[i]]

def isWinner(x, nums):
    marias_score = 0
    bens_score = 0
    primes = generate_primes(max(nums))
    
    for n in nums:
        if primes[1] >= n:
            # If there are no prime numbers <= n, Ben wins
            bens_score += 1
        else:
            # Otherwise, determine the winner of the game
            maria_wins = False
            for p in primes:
                if p > n:
                    break
                if n % p == 0:
                    maria_wins = not maria_wins
            if maria_wins:
                marias_score += 1
            else:
                bens_score += 1
    
    if marias_score > bens_score:
        return "Maria"
    elif bens_score > marias_score:
        return "Ben"
    else:
        return None
