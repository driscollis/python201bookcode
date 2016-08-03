from itertools import combinations_with_replacement

for item in combinations_with_replacement('WXYZ', 2):
    print(''.join(item))