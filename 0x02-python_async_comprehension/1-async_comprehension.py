#!/usr/bin/env python3
"""sync_comprehension"""

from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random float numbers
    between 0 and 10 using async comprehension over async_generator.

    Returns:
        List[float]: a list of 10 random float numbers between 0 and 10
    """
    result = [i async for i in async_generator()]
    return result
