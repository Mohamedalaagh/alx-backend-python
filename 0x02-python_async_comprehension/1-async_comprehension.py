#!/usr/bin/env python3
"""Import async_generator from previous task and write a coroutine
that takes no argumednts.

return the 10 random numbers from random number.
"""


from typing import List


async def async_comprehension() -> List[float]:
    '''returns a list of rand numbers using async comprehension'''

    async_gen = __import__('0-async_generator').async_generator

    rand_num = [k async for k in async_gen()]

    return rand_num


if __name__ == '__main__':
    import asyncio

    print(asyncio.run(async_comprehension()))
