"""
Starting in the top left corner of a 2×2 grid, and only being able
to move to the right and down, there are exactly 6 routes to
the bottom right corner.
How many such routes are there through a 20×20 grid?

https://projecteuler.net/problem=15
"""
import time


move_dict = {(0, 0): 0,
             (1, 0): 1,
             (0, 1): 1}             # To be used by memoization function


def factorial(n: int) -> int:
    """Returns factorial of n."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def num_routes_comb(m: int, n: int) -> int:
    """Calculates number of routes to traverse a lattice of size m x n using Combinations.

    For a lattice of size (m x n), m + n moves are needed to traverse between 2 corners.
    Out of those, m moves will always be in one direction (right or down)
    And n moves will always be in one direction (right or down)
    Given these constraints, the total no. of routes possible =
    (m + n)! / (m! * n!)
    """
    return int(factorial(m + n) / (factorial(m) * factorial(n)))


def num_routes_memo(m: int, n: int) -> int:
    """Calculates number of routes to traverse a lattice of size m x n using Memoization."""
    if (m, n) in move_dict:
        return move_dict[(m, n)]

    move_dict[(0, n)] = 1               # Only 1 possible path once we reach the edge
    move_dict[(m, 0)] = 1               # Only 1 possible path once we reach the edge

    move_dict[(m, n)] = num_routes_memo(m, n-1) + num_routes_memo(m-1, n)
    return move_dict[(m, n)]


if __name__ == '__main__':
    t0 = time.time()
    print(num_routes_comb(20, 20))
    print('Solved in {} seconds using {}'.format(time.time()-t0, num_routes_comb.__name__))

    t0 = time.time()
    print(num_routes_memo(20, 20))
    print('Solved in {} seconds using {}'.format(time.time()-t0, num_routes_memo.__name__))
