"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5
"""


def min_div_by_range(x, y):
    """Smallest positive number, evenly divisible by all numbers between x and y."""
    num = y
    while True:
        for i in range(x, y+1):
            if num % i != 0:
                break
            elif num % i == 0 and i == y:
                return num
        num += y                        # Because it has to be divisible by y


if __name__ == '__main__':
    print('Calculating...')
    print(min_div_by_range(1, 20))
