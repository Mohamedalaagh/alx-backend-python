#!/usr/bin/env python3
"""
 # Async Generator Module

This module provides an asynchronous generator that yields random floating-point numbers between 0 and 10.

## Functionality

### async_generator

```python
async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time"""
"""


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
