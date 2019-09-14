"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""
from math import sqrt


def is_prime(x: int) -> bool:
    """Returns True if 'x' is prime."""
    return not any(x % j == 0 for j in range(x-1, 1, -1))


def largest_prime_factor_of(n: int) -> int:
    """Finds the largest prime factors of 'n'."""
    for i in range(int(sqrt(n) + 1), 0, -1):              # It will kill my processor if I don't square root!
        if n % i == 0 and is_prime(i):
            return i


if __name__ == '__main__':
    n = 600851475143
    print('Calculating largest prime factor of {}...'.format(n))
    print('Tada ->', largest_prime_factor_of(n))
