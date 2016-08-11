# Python 3.4 coroutine example
import asyncio

@asyncio.coroutine
def my_coro():
    yield from func()