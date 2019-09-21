"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

https://projecteuler.net/problem=22
"""
import time


def build_list() -> list:
    """Builds a sorted list using names.txt."""
    with open('euler022_names.txt') as file:
        contents = file.read()
        name_list = contents.replace('"', '').split(',')
        name_list.sort()
        return name_list


def word_value(word: str) -> int:
    """Returns the word value for a string.

    A = 1, B = 2 ... CAB = 3 + 1 + 2 = 6
    """
    value = 0
    for char in word:
        value += ord(char) - 64    # ord ('A') = 65
    return value


def build_dict(name_list: list) -> dict:
    """Builds a dictionary using a sorted named list.

    Key = Name,
    Value = [order in list, name value, name score]
    """
    name_dict = {}
    for i, name in enumerate(name_list):
        name_dict[name] = [i + 1, word_value(name), (i + 1) * word_value(name)]
    return name_dict


def sum_name_scores(name_dict: dict) -> int:
    """Returns the sum of all the name scores in a dictionary."""
    total = 0
    for k, v in name_dict.items():
        total += v[2]
    return total


if __name__ == '__main__':
    t0 = time.time()
    print(sum_name_scores(build_dict(build_list())))
    print('Solved in {} seconds'.format(time.time()-t0))
