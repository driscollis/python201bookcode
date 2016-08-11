import threading

total = 0

def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    total += amount
    print (total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()