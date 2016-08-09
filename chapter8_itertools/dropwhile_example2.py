from itertools import dropwhile

def greater_than_five(x):
    return x > 5

print(list(dropwhile(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))