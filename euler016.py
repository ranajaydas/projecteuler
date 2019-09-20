"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16
"""
import time


def sum_digits(n: int) -> int:
    """Returns sum of digits of n."""
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


if __name__ == '__main__':
    t0 = time.time()
    print(sum_digits(2**1000))
    print('Solved in {} seconds using {}'.format(time.time()-t0, sum_digits.__name__))
