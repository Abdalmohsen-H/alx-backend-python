#!/usr/bin/env python3
""" async comprehension generator module docs for task 1 """
from typing import List

zero_async_gen = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async compre. generator function doc
    task 1"""
    return [rand_flt async for rand_flt in zero_async_gen()]
