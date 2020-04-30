"""
Plus Minus

https://www.hackerrank.com/challenges/plus-minus/problem
"""


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for n in arr:
        if n > 0:
            positive += 1
        elif n == 0:
            zero += 1
        else:
            negative += 1

    tot = sum([positive, negative, zero])

    print(1. * positive / tot)
    print(1. * negative / tot)
    print(1. * zero / tot)
