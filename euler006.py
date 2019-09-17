"""
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Their difference is 2640

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum

https://projecteuler.net/problem=6
"""


def sum_of_square_to(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i ** 2
    return total


def square_of_sum_to(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i
    return total ** 2


if __name__ == '__main__':
    n = 100
    print(square_of_sum_to(n) - sum_of_square_to(n))

