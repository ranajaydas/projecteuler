"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def sum_mul_below(listofmuls: list, n: int) ->int:
    """Returns sum of all the multiples of 'listofmuls' below 'n'."""
    total = 0
    for i in range(n):
        for mul in listofmuls:
            if i % mul == 0:
                total += i
                break
    return total


if __name__ == '__main__':
    print(sum_mul_below(listofmuls=[3, 5], n=1000))
