#!/usr/bin/env python3
"""Update Data notations"""
from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """First element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
