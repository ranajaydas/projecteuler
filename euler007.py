"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

https://projecteuler.net/problem=7
"""
import math


def is_prime(x: int) -> bool:
    """Returns True if the number is prime."""
    return not any(x % i == 0 for i in range(2, int(math.sqrt(x)+1)))


def nth_prime(n: int) -> int:
    """Returns the nth prime number, 2 being the first prime."""
    last_found = 0
    primes_found = 0
    while primes_found <= n:
        last_found += 1
        if is_prime(last_found):
            primes_found += 1
    return last_found


if __name__ == '__main__':
    print(nth_prime(10001))


