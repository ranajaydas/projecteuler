"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21
"""
import time

amicable_list = []


def sum_of_divisors(n: int) -> int:
    """Returns the sum of all the proper divisors of 'n'."""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def is_amicable(n: int) -> bool:
    """Returns True if the number forms an amicable pair. Stores the pair in a global var."""
    global amicable_list
    if n in amicable_list:
        return True
    x = sum_of_divisors(n)
    y = sum_of_divisors(x)
    if n == y and n != x:
        amicable_list += [x] + [y]
        return True
    return False


def sum_all_amicable_under(n: int):
    """Finds all the amicable numbers under n and returns their sum."""
    for i in range(1, n+1):
        is_amicable(i)
    return sum(amicable_list)


if __name__ == '__main__':
    t0 = time.time()
    print(sum_all_amicable_under(10000))
    print(amicable_list)
    print('Solved in {} seconds'.format(time.time()-t0))
