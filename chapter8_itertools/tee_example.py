from itertools import tee

data = 'ABCDE'
iter1, iter2 = tee(data)

for item in iter1:
    print(item)

for item in iter2:
    print(item)