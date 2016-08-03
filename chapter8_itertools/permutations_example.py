from itertools import permutations

for item in permutations('WXYZ', 2):
    print(''.join(item))