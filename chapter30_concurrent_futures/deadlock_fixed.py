from concurrent.futures import ThreadPoolExecutor


def wait_forever():
    """
    This function will wait forever if there's only one
    thread assigned to the pool
    """
    my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])

    return my_future

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)
    fut = executor.submit(wait_forever)

    result = fut.result()
    print(list(result.result()))