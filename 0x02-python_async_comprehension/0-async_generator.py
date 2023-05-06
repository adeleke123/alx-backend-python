#!/usr/bin/env python3
"""Async generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine function that asynchronously yields 10 random numbers
    between 0 and 10 after each second delay.

    Yields:
        float: random float number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)  # asynchronously wait for 1 second
        yield random.uniform(0, 10)  # generate random float num btw 0 & 10
