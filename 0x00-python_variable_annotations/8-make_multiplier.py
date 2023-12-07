#!/usr/bin/env python3
"""Returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns the multiplier function"""
    def multiplier_function(value: float) -> float:
        """Returns multiplcation of two floats"""
        return value * multiplier

    return multiplier_function
