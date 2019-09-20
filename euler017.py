"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

https://projecteuler.net/problem=17
"""
import time


ones_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def wordify(n: int) -> str:
    """Converts an integer into an English string."""
    string = ''
    temp_num = n

    if temp_num // 1000:
        string += ones_list[temp_num // 1000] + ' thousand '
        temp_num = temp_num % 1000

    if temp_num // 100:
        string += ones_list[temp_num // 100] + ' hundred '
        temp_num = temp_num % 100

    if n > 100 and n % 100:
        string += 'and '

    if temp_num // 10 > 1:
        string += tens_list[temp_num // 10] + ' '
        temp_num = temp_num % 10
        string += ones_list[temp_num]

    elif temp_num // 10 == 1:
        string += teens_list[temp_num-10]

    else:
        temp_num = temp_num % 10
        string += ones_list[temp_num]

    return string


def sum_of_chars_upto(n: int) -> int:
    """ Sums up the number of characters in all the numbers upto n."""
    total = 0
    for i in range(1, n+1):
        total += len(wordify(i).replace(' ', ''))
    return total


if __name__ == '__main__':
    t0 = time.time()
    print(sum_of_chars_upto(1000))
    print('Solved in {} seconds using {}'.format(time.time()-t0, sum_of_chars_upto.__name__))
