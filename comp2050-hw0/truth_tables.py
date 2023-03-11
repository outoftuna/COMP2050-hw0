""" File name:   truth_tables.py
    Author:      Ta Viet Thang 
    Date:        Mar 11, 2023
    Description: This file defines a number of functions which implement Boolean
                 expressions.

                 It also defines a function to generate and print truth tables
                 using these functions.

                 It should be implemented for Exercise 2 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
from typing import Callable


def boolean_fn1(a:bool, b:bool, c:bool) -> bool:
    """ Return the truth value of (a ∨ b) → (-a ∧ -b) """
    return not(a or b) or ((not a) and (not b))


def boolean_fn2(a:bool, b:bool, c:bool) -> bool:
    """ Return the truth value of (a ∧ b) ∨ (-a ∧ -b) """
    return not(a and b) or ((not a) and (not b))


def boolean_fn3(a:bool, b:bool, c:bool) -> bool:
    """ Return the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b) """
    return ((not c or a) and (a and not b)) or (not a and b)


def draw_truth_table(boolean_fn:Callable) -> None:
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None

        If your function is working correctly, your console output should look
        like this:

        >>> from truth_tables import *
        >>> draw_truth_table(boolean_fn1)
        a     b     c     res
        -----------------------
        False False False True
        False False True  True
        False True  False False
        False True  True  False
        True  False False False
        True  False True  False
        True  True  False False
        True  True  True  False
    """
    print('a\t b\t c\t res')
    print('----------------------')
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                print(a, '\t', b, '\t', c, '\t', boolean_fn(a,b,c))

if __name__ == "__main__":
    print("boolean_fn1")
    draw_truth_table(boolean_fn1)
    print("boolean_fn2")
    draw_truth_table(boolean_fn2)
    print("boolean_fn3")
    draw_truth_table(boolean_fn3)