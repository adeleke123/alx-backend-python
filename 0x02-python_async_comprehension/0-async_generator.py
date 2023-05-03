#!/usr/bin/env python3

"""
A Python module to generate 10 random float numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def generate_float_numbers() -> AsyncGenerator[float, None]:
    """
    Generate 10 random float numbers asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    async for number in generate_float_numbers():
        print(number)


if __name__ == "__main__":
    asyncio.run(main())

