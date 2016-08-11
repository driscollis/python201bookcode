import asyncio
import functools


def event_handler(loop, stop=False):
    print('Event handler called')
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(functools.partial(event_handler, loop))
        print('starting event loop')
        loop.call_soon(functools.partial(event_handler, loop, stop=True))

        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close()