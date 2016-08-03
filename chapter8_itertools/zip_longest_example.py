from itertools import zip_longest

for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print (item)