"""
The Matrix Script

https://www.hackerrank.com/challenges/matrix-script/problem
"""

# The problem doesn't allow us to use if statements, so we need to get
# creative...
def decode_matrix(matrix, rows, cols):
    transposed_matrix = []

    for col in range(cols):
        # Transposing the matrix
        t = []
        for row in range(rows):
            t.append(matrix[row][col])
        transposed_matrix.extend(t)

    # For each index, finding out if it is an alphanumeric character
    matrix_mask = list(map(lambda c: c.isalnum(), transposed_matrix))

    # No alphanumeric character? Just return the original string
    try:
        first_alphanum = matrix_mask.index(True)
    except ValueError:
        return "".join(transposed_matrix)

    alphanum_indexes = []

    # Keep going as long as we have any alphanumeric value
    while any(list(map(lambda i: i, matrix_mask))):

        try:
            alphanum = matrix_mask.index(True)
            # We guess this will be the last, can always change our mind later
            last_alphanum = alphanum

            # Change to None so we pick the next value each time
            matrix_mask[alphanum] = None

            alphanum_indexes.append(alphanum - first_alphanum)
        except ValueError:
            # No more left,
            pass

    # Breaking into head, body and tail
    head = transposed_matrix[:first_alphanum]
    body = transposed_matrix[first_alphanum:last_alphanum + 1]
    tail = transposed_matrix[last_alphanum + 1:]

    # Finding the indexes of the special characters in the body as those
    # which are not alphanumeric
    indexes_specials_chars_in_body = list(
        set(range(len(body))) - set(alphanum_indexes)
    )

    # Replacing them all with strings
    for i in indexes_specials_chars_in_body:
        body[i] = ' '

    # Making into a list and splitting on whitespaces
    body = "".join(body).split(" ")
    # ...to remove consecutive whitespaces
    body = list(filter(lambda i: i != '', body))

    # Concatenating and returning
    text = "".join(head) + " ".join(body) + "".join(tail)

    return text


matrix = ["# ",
          " @"]

print(decode_matrix(matrix, 2, 2))
