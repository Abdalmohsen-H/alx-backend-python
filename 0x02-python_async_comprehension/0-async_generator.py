#!/usr/bin/env python3
""" task 0 : async generator Module doc. """
import asyncio
import random
from typing import async_generator


async def async_generator() -> async_generator[float, None, None]:
    """ func documentation here just random gen. 
    The return type of generator functions can be
    annotated by the generic type Generator[yield_type,
    send_type, return_type] provided by typing.py module
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)    