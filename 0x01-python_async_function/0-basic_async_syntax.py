#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes in an integer argument and returns a float value"""

    # Generate a random float(rand_f) between 0 & the maximum delay
    rand_f = random.uniform(0, max_delay)
    await asyncio.sleep(rand_f)

    # Return the generated random float (rand_f)
    return rand_f
