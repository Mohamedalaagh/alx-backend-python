#!/usr/bin/env python3
"""Import async_generator from previous task and write a coroutine
that takes no argumednts.

return the 10 random numbers from random number.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
