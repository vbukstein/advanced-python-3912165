# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable, batched

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain("ABCD", "1234")
print(list(x))

# make a prepend function
def prepend(val, iterable):
    return itertools.chain([val], iterable)

result = prepend(5, [1, "A", True, 10])
print(list(result))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']
result = itertools.chain.from_iterable([s1,s2,s3])
print(list(result))

# batched() takes an iterable and breaks it into chunks
vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
batches = list(itertools.batched(vals, 5))
print(batches)

# batched can be used to reshape iterables
original = [(0,1), (2,3), (4,5), (6,7)]
result = itertools.batched(itertools.chain.from_iterable(original), 4)
print(list(result))
