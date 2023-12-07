#!/usr/bin/env python3
"""
A module containing a function for safely getting a value from a dictionary.
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
