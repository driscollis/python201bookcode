import threading

total = 0
lock = threading.RLock()

def do_something():

    with lock:
        print('Lock acquired in the do_something function')
    print('Lock released in the do_something function')

    return "Done doing something"

def do_something_else():
    with lock:
        print('Lock acquired in the do_something_else function')
    print('Lock released in the do_something_else function')

    return "Finished something else"


def main():
    with lock:
        result_one = do_something()
        result_two = do_something_else()

    print (result_one)
    print (result_two)


if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=main)
        my_thread.start()