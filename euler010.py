"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

https://projecteuler.net/problem=10
"""
import math
import time


def is_prime(x: int) -> bool:
    """Returns True if the number is prime."""
    return not any(x % i == 0 for i in range(2, int(math.sqrt(x)+1)))


def sum_prime_to(n: int) -> int:
    """Sums all primes below n."""
    total = 5
    for i in range(5, n, 2):
        if is_prime(i):
            total += i
    return total


if __name__ == '__main__':
    t0 = time.time()
    print(sum_prime_to(2000000))
    print('Solved in {} seconds'.format(time.time()-t0))
