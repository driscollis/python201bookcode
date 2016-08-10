# silly_functions.py
import time

@profile
def fast_function():
    print("I'm a fast function!")

@profile
def slow_function():
    time.sleep(2)
    print("I'm a slow function")

if __name__ == '__main__':
    fast_function()
    slow_function()