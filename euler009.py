"""A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for
which a + b + c = 1000. Find the product abc.

https://projecteuler.net/problem=9
"""
import math


def pyth_triplet_prod(sum: int):
    """Finds product of pythagorean triplet whose sum is 'sum'."""
    for a in range(1, sum):
        for b in range(a, sum):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == sum:
                return int(a * b * c)


if __name__ == '__main__':
    print(pyth_triplet_prod(1000))
