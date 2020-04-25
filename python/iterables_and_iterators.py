"""
Iterables and Iterators

https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""
from itertools import combinations
from math import factorial

def compute_probability(num_items, sequence, num_indices):
    indexes = set()

    # O(N) way of retrieving indexes
    i = 0
    for e in sequence:

        if e == " ":
            continue

        if e == 'a':
            indexes.add(i)

        i += 1

    # Leveraging itertools to obtain combinations
    possibilities = map(set, combinations(range(num_items), num_indices))

    # Filtering only those which include the indexes corresponding to the
    # letter a
    valids = filter(lambda p: len(p.intersection(indexes)) > 0, possibilities)
    num_valids = sum(1 for _ in valids)
    # n! / (r! * (n - r)!)

    # We have exhausted the iterator, but the number of combinations can be
    # obtained via formula rather than having to regenerate all of them
    num_possibilities = 1. * factorial(num_items) / (factorial(num_indices)
                                                     * factorial(num_items -
                                                                 num_indices))
    return 1. * num_valids / num_possibilities

print(compute_probability(4, "a a c d", 2))
