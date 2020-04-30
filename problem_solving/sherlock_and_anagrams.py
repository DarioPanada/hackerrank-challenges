"""
Sherlock and Anagrams

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

from collections import Counter
from math import factorial


def sherlockAndAnagrams(s):
    tot_pairs = 0

    # Going through each possible substring length except one which would be
    # the string itself
    for substring_length in range(len(s) - 1):
        # Generating substrings
        substrings = [s[i:i + substring_length + 1]
                      for i in range(0, len(s) - substring_length)]
        # Sorting them, as two sorted agrams produce the same string
        substrings_sorted = ["".join(sorted(s)) for s in substrings]

        # Counting occurrences
        occurrences = Counter(substrings_sorted)

        # For those substrings which occur more than once, those are our
        # agrams. How many combinations of them can we make?
        #  nCr = n! / r! * (n - r)!,
        pairs = sum(factorial(o) / (factorial(2) * (factorial(o - 2)))
                    for p, o in occurrences.items() if o > 1)
        tot_pairs += pairs

    return tot_pairs


sherlockAndAnagrams("cdcd")
