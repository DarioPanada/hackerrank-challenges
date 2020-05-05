"""
Sherlock and the Valid String

https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
"""

from collections import Counter


def isValid(s):
    # Number of times each letter occurs
    letter_occurrences = Counter(s)
    # Number of times each occurrence occurs
    occurrences_o = Counter(letter_occurrences.values())

    if len(list(occurrences_o.keys())) > 2:
        return "NO"

    if len(list(occurrences_o.keys())) == 1:
        return "YES"

    # First, the occurrence of occurrences has to be within 1 of each other,
    # or here has to be a possibili of eliminating a SINGLE letter altogether.
    occurrences = list(occurrences_o.keys())

    if abs(occurrences[0] - occurrences[1]) > 1 \
            and (1 not in occurrences or (1 in occurrences and
                                          occurrences_o[1] > 1)):
        return "NO"

    # And there can be at most one letter that has to be adjusted
    num_letters = occurrences_o.values()

    if 1 not in num_letters:
        return "NO"

    return "YES"


print(isValid("aaaaabc"))
