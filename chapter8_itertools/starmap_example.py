from itertools import starmap

def add(a, b):
    return a+b

for item in starmap(add, [(2,3), (4,5)]):
    print(item)