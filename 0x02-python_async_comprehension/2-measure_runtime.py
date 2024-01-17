#!/usr/bin/env python3
""" task 2 Module : measure runtime of async comprehension
 generator """
import asyncio
import time

async_comp_gen = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function to measure runtime of async comprehension
    generator """
    start_timestamp = time.perf_counter()
    await asyncio.gather(async_comp_gen(), async_comp_gen(), async_comp_gen(),
                         async_comp_gen()
                         )
    # or
    # jobs = [async_comp_gen() for _ in range(4)]
    # await asyncio.gather(*jobs)

    end_timestamp = time.perf_counter()
    duration = end_timestamp - start_timestamp
    return duration
