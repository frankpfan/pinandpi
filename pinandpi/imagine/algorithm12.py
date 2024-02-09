'''
pynandpi.misc.algorithm

Note
----
46_0000_0000 needles -> about (1+0.0008%)*pi
'''

from math import sin, radians
from random import seed, uniform


def im(y, d):
    if y == 0:
        return 1
    dy = sin(radians(d))
    ry = y + dy
    if ry >= 2 or ry <= 0:
        return 1
    return 0


def th(x=100_0000):  # 44s, 1*10^8
    n = 0
    i = 0
    for _ in range(x):
        n += 1
        i += im(uniform(0, 2), uniform(0, 360))
    return n, i


def main():
    nt, it = 0, 0
    while True:
        seed()
        res = th(1000_0000)
        nt += res[0]
        it += res[1]
        print('{:>8}*10^6{:12}{:24.15f}'.format(nt//(10**6), it, nt/it))


if __name__ == '__main__':
    main()
