#!/usr/bin/env python3
""" task 0 : async generator Module doc. """

import asyncio
import random
from typing import async_generator


async def async_generator() -> async_generator[float, None, None]:
    """ func documentation here just random gen. """
    for _ in range(10):
        # await with asyncio for 1 sec asynchronously
        await asyncio.sleep(1)
        yield random.uniform(0, 10)    