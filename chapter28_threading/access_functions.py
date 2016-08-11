import threading

total = 0
lock = threading.Lock()


def do_something():
    lock.acquire()

    try:
        print('Lock acquired in the do_something function')
    finally:
        lock.release()
        print('Lock released in the do_something function')

    return "Done doing something"

def do_something_else():
    lock.acquire()

    try:
        print('Lock acquired in the do_something_else function')
    finally:
        lock.release()
        print('Lock released in the do_something_else function')

    return "Finished something else"

if __name__ == '__main__':
    result_one = do_something()
    result_two = do_something_else()