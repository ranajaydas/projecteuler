"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=3
"""


def is_palindrome(x: int) -> bool:
    """Returns true if a number is a palindrome."""
    num_digits = len(str(x))                    # Calculate number of digits in a number
    for i in range(int(num_digits/2)):
        if str(x)[i] != str(x)[-1-i]:           # Check the first and last digit and move inwards
            return False
    return True


def largest_palindrome(x: int, y: int, stop: int = 1) -> tuple:
    """Returns largest palindrome (and multiples) from the product of any numbers below x and y (incl)."""
    palindrome_dict = {}
    for i in range(x, stop, -1):
        for j in range(y, stop, -1):
            if is_palindrome(i*j):
                palindrome_dict[i*j] = [i, j]

    largest = sorted(palindrome_dict)[-1]       # The largest palindrome number found
    multiple1 = palindrome_dict[largest][0]     # The numbers that multiplied to the make it
    multiple2 = palindrome_dict[largest][1]     # The numbers that multiplied to the make it

    return largest, multiple1, multiple2


if __name__ == '__main__':
    x, y = 999, 999
    stop = 100
    print('The largest palindrome made from the product of numbers below {} and {}:'.format(x, y))
    print('{} made from the product of {} and {}'.format(*largest_palindrome(x, y)))
