#!/usr/bin/env python3
"""Unions and tupple"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    return (k, v**2)
