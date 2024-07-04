#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    m_wins, b_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    prime_nums = [True for _ in range(1, n + 1, 1)]
    prime_nums[0] = False
    for i, is_prime in enumerate(prime_nums, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime_nums[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, prime_nums[0: n])))
        b_wins += primes_count % 2 == 0
        m_wins += primes_count % 2 == 1
    if m_wins == b_wins:
        return None
    return 'Maria' if m_wins > b_wins else 'Ben'
