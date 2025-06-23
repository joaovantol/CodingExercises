def generatePrimeList(n: int) -> list[int]:
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for prime number generation

    Returns:
        list: A list of prime numbers ≤ n
    """
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*current :: current] = [False] * len(sieve[current*current :: current])

    return [i for i, isPrime in enumerate(sieve) if isPrime]

def countCircularPrimes(limit: int) -> int:
    """
    Count the number of circular primes below the given limit.

    Args:
        limit (int): The upper bound for checking circular primes

    Returns:
        int: Count of circular primes below the limit
    """
    primes = set(generatePrimeList(limit - 1))
    circularPrimes = set()

    for prime in primes:
        if prime in circularPrimes:
            continue

        s = str(prime)
        rotations = {int(s[i:] + s[:i]) for i in range(len(s))}

        if all(rot in primes for rot in rotations):
            circularPrimes.update(rotations)

    return len(circularPrimes)