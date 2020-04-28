"""
Maximize it!

https://www.hackerrank.com/challenges/maximize-it/problem
"""

from itertools import product


def maximize_it(modulus, lists):
    # Squaring and modding to save computation and time

    lists = map(lambda l: map(lambda x: (x ** 2) % modulus, l), lists)
    # Finding every possible combination
    possibilities = product(*lists)
    # Summing
    sum_of_possibilities = map(sum, possibilities)
    # Modding
    sum_of_possibilities_modded = map(lambda s: s % modulus,
                                      sum_of_possibilities)
    return max(sum_of_possibilities_modded)


n, mod = map(int, input().split(" "))
lists = []

for _ in range(n):
    lists.append(map(int, input().split(" ")[1:]))

print(maximize_it(mod, lists))
