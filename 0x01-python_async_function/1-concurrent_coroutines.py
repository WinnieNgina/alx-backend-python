#!/usr/bin/env python3
""""""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    my_list = []
    for i in range(n):
        rand = await wait_random(max_delay)
        my_list.append(rand)
    return sorted(my_list)
