#!/usr/bin/env python3
"""Mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Returns their sum as a float."""
    return float(sum(mxd_lst))
