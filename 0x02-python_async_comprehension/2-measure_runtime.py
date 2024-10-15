#!/usr/bin/env python3
"""Import async_comprehension from the previous task and
generrate a measure runtime.
"""


import asyncio
import time


async def measure_runtime() -> float:
    '''Runs async comprehension in parallel and returns the total time'''
    comp = __import__('1-async_comprehension').async_comprehension

    st = time.time()
    await asyncio.gather(comp(), comp(), comp(), comp())

    return time.time() - st


if __name__ == '__main__':
    print(asyncio.run(measure_runtime()))
