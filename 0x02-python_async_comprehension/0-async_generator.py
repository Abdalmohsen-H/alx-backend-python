#!/usr/bin/env python3
""" task 0 : async generator Module doc. """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """ func documentation here just random gen. """
    for _ in range(10):
        # await with asyncio for 1 sec asynchronously
        await asyncio.sleep(1)
        yield random.uniform(0, 10)    