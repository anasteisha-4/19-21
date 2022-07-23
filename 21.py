from functools import *


def m(h):
    a, b = h
    return (a * 2, b), (a, b * 2), (a + 3, b), (a, b + 3)


@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 227:
        return 'w'
    if any(g(x) == 'w' for x in m(h)):
        return 'i1'
    if all(g(x) == 'i1' for x in m(h)):
        return 'd1'
    if any(g(x) == 'd1' for x in m(h)):
        return 'i2'
    if all(g(x) == 'i1' or g(x) == 'i2' for x in m(h)):
        return 'd2'


for G in range(1, 216):
    znach = g((5, G))
    if znach == 'd2':
        print(G)
        break
