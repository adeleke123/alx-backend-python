#!/usr/bin/env python3
"""Measure the runtime"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    takes two integer arguments n and max_delay, and returns a float
    representing the average time it takes to execute wait_n(n, max_delay)
    """

    # Measure the start time(s_time)
    s_time = perf_counter()

    # Run the wait_n function and measure the elapsed time(e_time)
    asyncio.run(wait_n(n, max_delay))
    e_time = perf_counter() - s_time

    # Return the average time per n
    return e_time / n
