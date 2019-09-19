"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

https://projecteuler.net/problem=14
"""
import time


collatz_length_dict = {1: 1,
                       2: 2
                       }


def collatz_length(num: int) -> int:
    length = 0
    n = num
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n = n // 2
        length += 1
        if n in collatz_length_dict:
            collatz_length_dict[num] = length + collatz_length_dict[n]      # Build the dictionary
            return length + collatz_length_dict[n]


def max_chain():
    for i in range(1, 1000000):
        collatz_length(i)
    print(max(collatz_length_dict, key=collatz_length_dict.get))


if __name__ == '__main__':
    t0 = time.time()
    max_chain()
    print('Solved in {} seconds'.format(time.time()-t0))
