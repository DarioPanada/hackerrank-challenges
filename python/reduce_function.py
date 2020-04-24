"""
Reduce function

https://www.hackerrank.com/challenges/reduce-function/problem
"""
from __future__ import print_function
from fractions import Fraction
from fractions import gcd

def multiply_and_simplify(frac_tmp, new_frac):
    numerator = frac_tmp.numerator * new_frac.numerator
    denominator = frac_tmp.denominator * new_frac.denominator

    g = gcd(numerator, denominator)

    return Fraction(numerator/g, denominator/g)

def product(fracs):
    t = reduce(multiply_and_simplify, fracs, Fraction(1,1))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)
