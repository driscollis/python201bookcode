from itertools import compress


letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))