from concurrent.futures import ThreadPoolExecutor


def wait_forever():
    """
    This function will wait forever if there's only one
    thread assigned to the pool
    """
    my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
    result = my_future.result()
    print(result)

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(wait_forever)