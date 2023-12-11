#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay them returns the random value"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
