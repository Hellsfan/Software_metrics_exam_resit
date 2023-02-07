"""
Exam Resit for Software Metrics
implementation of the math function math.isfinite()
"""
import math


def is_finite(input_arg):
    """Return True if x is neither an infinity nor a NaN, and False otherwise."""
    if input_arg is None:
        raise TypeError("No arguments were given to the method! Method requires a float or int argument!")
    if not isinstance(input_arg, (int, float)):
        raise TypeError(f"Given argument is not valid. Arugment should be int or float! Your input: {type(input_arg)}")
    return math.isfinite(input_arg)


is_finite(5)
