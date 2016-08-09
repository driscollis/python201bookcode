from itertools import dropwhile

print(list(dropwhile(lambda x: x<5, [1,4,6,4,1])))