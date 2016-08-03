from itertools import count, islice

for i in islice(count(), 3, 15):
    print(i)