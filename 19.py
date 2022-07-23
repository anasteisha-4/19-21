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
    if any(g(x) == 'i1' for x in m(h)):
        return 'd1'


for G in range(1, 216):
    znach = g((5, G))
    if znach == 'd1':
        print(G)
        break
