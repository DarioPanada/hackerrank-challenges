"""
The Minion Game

https://www.hackerrank.com/challenges/the-minion-game/problem
"""


def count_substrings(start_string, start_with_consonant):
    """
    Counts the number of possible substrings that can be made out of a
    string considering only substrings beginning with a vowel of consonant.

    Eg: BANANA, considering substrings starting with a vowel.

    A x3, AN x2, ANA x 2, ANAN x1, ANANA x1
    Total = 9

    Parameters
    ----------
    start_string : string
        The initial string
    start_with_consonant : bool
        Set to True if you want to consider words starting with a consonant,
        False otherwise

    Returns
    -------
    int
        The total number of substring
    """
    # A letter is valid if it is not the case that it is a vowel and we said
    # substrings should start with a consonant.
    valid_letter = lambda letter: (letter in ['A', 'E', 'I', 'O', 'U']) ^ \
                                  start_with_consonant

    num_letters = len(start_string)

    # Maps each letter in the original strig to a boolean to indicate if it
    # is a candidate to start a substring

    # For example, with BANANA and start_with_consonant=False we obtain
    # [False, True, False, True, False, True]
    start_string_bool = map(valid_letter, start_string)

    # The logic here is that if a string has n characters, and the substring
    # begins at position i, then it can create n - i substrings. Eg: BANANA
    # has n = 6. If we consider the first N, we can create 4 substrings: N, NA,
    # NAN and NANA. The first N has i = 2, and 6 - 2 = 4.

    # Any loop iteration is too slow. We exploit map.

    # Create a vector from 1 to the length of the string inclusive,
    # in descending order.
    indexes = reversed(range(1, num_letters + 1))

    # Dot product of our indexes vector by our boolean vector. The resulting
    # vector will have the index of each valid letter in the position where
    # this occurs, and 0s otherwise.

    # Remember BANANA produced [False, True, False, True, False, True], then
    # [False, True, False, True, False, True] * [6, 5, 4, 3, 2, 1] =
    # [0, 5, 0, 3, 0, 1]
    products = map(lambda x, y: x * y, start_string_bool, indexes)

    # If we look at the products vector: [0, 5, 0, 3, 0, 1]
    # The 5 represents the number of substrings we can create with the first
    # A (ANANA, NANA, ANA, NA, A), the 3 with the second A (ANA, NA, A) and
    # the 1 with the last A (A).

    # So, we just need to sum this
    score = sum(products)

    return score


def minion_game(string):
    stuart_score = count_substrings(string, True)
    kevin_score = count_substrings(string, False)

    if stuart_score > kevin_score:
        print("Stuart " + str(stuart_score))
    elif stuart_score == kevin_score:
        print("Draw")
    else:
        print("Kevin " + str(kevin_score))


if __name__ == "__main__":
    # Small input
    minion_game("BANANA")
