#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes two integer arguments and returns a list of float values
    """

    # Create a list of coroutines, each calling wait_random(max_delay)
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Await the tasks in the order that they complete
    return [await task for task in asyncio.as_completed(tasks)]
