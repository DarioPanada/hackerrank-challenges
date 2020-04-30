"""
Validating Credit Card Numbers

https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT


def cc_valid(cc_num):
    # Start number a 4,5 or 6
    if not cc_num[0] in ['4', '5', '6']:
        return "Invalid"

    # Length is exactly 16
    if len(cc_num.replace("-", "")) != 16:
        return "Invalid"

    currentNum = -1
    repetitions = 0
    i = 0
    for n in cc_num:
        i += 1
        try:
            int(n)
        except ValueError:
            if not (n == "-" and i % 5 == 0):
                return "Invalid"
            i = 0

        if n == "-":
            continue

        # We need to check if we have more than 4 repeated values
        if n == currentNum:

            repetitions += 1

            if repetitions == 3:
                return "Invalid"
        else:
            currentNum = n
            repetitions = 0

    return "Valid"


nums = ["7165863385679329",
        "6175824393389297",
        "5252248277877418",
        "9563584181869815",
        "5179123424576876"]

for num in nums:
    print(cc_valid(num))
