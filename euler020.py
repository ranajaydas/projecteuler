"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20
"""
import time


def factorial(n: int) -> int:
    """Returns factorial of n."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def sum_digits(n: int) -> int:
    """Returns the sum of all the digits in a number."""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


if __name__ == '__main__':
    t0 = time.time()
    print(sum_digits(factorial(100)))
    print('Solved in {} seconds'.format(time.time()-t0))
