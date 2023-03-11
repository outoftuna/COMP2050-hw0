""" File name:   math_functions.py
    Author:      Ta Viet Thang
    Date:        Mar 11, 2023
    Description: This file defines a set of variables and simple functions.

                 It should be implemented for Exercise 1 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import math
ln_e = math.log(math.e)

twenty_radians = 20*math.pi/180

def quotient_ceil(numerator, denominator):
    """ 
    Returns the ceiling of the result of the division
    (number, number) -> int
    """
    return int(math.ceil(numerator/denominator))

def quotient_floor(numerator, denominator):
    """
    Returns the floor of the result of the division
    (number, number) -> int
    """
    return int(math.floor(numerator/denominator))

def manhattan(x1, y1, x2, y2):
    """ 
    Return the manhattan distance between two points (x1,y1) and (x2,y2)
    """
    return (abs(x1-x2)+abs(y1-y2))


