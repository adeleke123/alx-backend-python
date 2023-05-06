#!/usr/bin/env python3
"""Use regular function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    An asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay: integer represents the maximum amount of time
        the wait_random coroutine waits before returning.

    Returns:
        An asyncio.Task object that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
