"""
Absolute Permutation

https://www.hackerrank.com/challenges/absolute-permutation/problem
"""


def absolutePermutation(n, k):
    indexes = range(1, n + 1)

    # Base case, if k should be 0 then the smallest permutation is the natural
    # ordering of the numbers
    if k == 0:
        return ' '.join(map(str, indexes))

    # Given a list of numbers N from 1 to n, we generate two lists col_a and
    # col_b such that abs(n_i - col_a_i) = k
    col_a = list(range(k + 1, k + n + 1))
    col_b = list(range(1 - (k + 1), 1 - k + n + 1))

    # A bit of adjusting because it's base-1 index
    z_ind = col_b.index(0)
    del col_b[z_ind]

    perm = []

    zipped_col = zip(col_a, col_b)

    # Switch list every k items
    use_a = False
    for i, (a, b) in enumerate(zipped_col):
        if i % k == 0:
            use_a = not use_a

        if use_a:
            perm.append(a)
        else:
            perm.append(b)

    # Conditions are the difference between every element in the permutation
    # list and its position should be equal to k AND that numbers should be
    # in the range 1 to n inclusive.
    diffs_equal_k = map(lambda n, i: abs(n - i), indexes, perm)
    diffs_acceptable = map(lambda n: n in indexes, perm)
    if all(diffs_equal_k) and all(diffs_acceptable):
        return ' '.join(map(str, perm))

    return '-1'


input = [[2, 1],
         [10, 5],
         [7, 5],
         [2, 1],
         [2, 0],
         [2, 0],
         [1, 0],
         [10, 5],
         [10, 0],
         [6, 0]]

input_test_mem = [
    [10, 4],
    [10, 1]
]

print(absolutePermutation(2, 1))
