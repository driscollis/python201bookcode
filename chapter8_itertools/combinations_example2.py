from itertools import combinations

for item in combinations('WXYZ', 2):
    print(''.join(item))