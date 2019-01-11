L = ['a', 'b', 'c']
if any(c in L for c in ('q', 'z')):
    print('it\'s there!')
else:
    print('it\'s not in there!')

# it's not in there!

if any(c in L for c in ('q', 'c')):
    print('it\'s there!')
else:
    print('it\'s not in there!')

# it's there!