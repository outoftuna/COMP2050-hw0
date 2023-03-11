""" File name:   truth_tables.py
    Author:      
    Date:        
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
    # YOUR CODE HERE


def boolean_fn2(a:bool, b:bool, c:bool) -> bool:
    """ Return the truth value of (a ∧ b) ∨ (-a ∧ -b) """
    # YOUR CODE HERE


def boolean_fn3(a:bool, b:bool, c:bool) -> bool:
    """ Return the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b) """
    # YOUR CODE HERE


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
    # YOUR CODE HERE

if __name__ == "__main__":
    print("boolean_fn1")
    draw_truth_table(boolean_fn1)
    print("boolean_fn2")
    draw_truth_table(boolean_fn2)
    print("boolean_fn3")
    draw_truth_table(boolean_fn3)