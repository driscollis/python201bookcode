# This is a shadowed import example. Note that we named
# this module "math.py" which shadows Python's math module

import math

def square_root(number):
    return math.sqrt(number)

square_root(72)