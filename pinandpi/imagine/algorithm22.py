'''
pynandpi.imagine.algorithm2.2.1

New in version 2: numpy.

Note
----
2022/12 test: 46_0000_0000 needles -> about (1+0.0008%)*pi
         1*10^8 needles, 9% of i5 cpu: 3.2s, ~130MB memory
'''

import numpy as np


rng = np.random.default_rng()


def th(x=10**6):     # 1*10^8 needles, 9% of i5 cpu: 3.2s, ~130MB memory
    y_arr = rng.uniform(0., 2., (x,))
    dy_arr = np.sin(rng.uniform(0., np.pi, (x,)))
    b_arr = (y_arr - dy_arr) <= 0
    return x, np.sum(b_arr, dtype='i8')


def main():
    n = 0
    i = 0
    while True:
        for _ in range(200):
            dn, di = th(10**6)
            n += dn
            i += di
        print('{:>8}*10^8 {:16} {:21.15f}'.format(n//(10**8), i, n/i))


if __name__ == '__main__':
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt.\nDone.')
        input('回车以退出... ')
        sys.exit(0)
    except Exception:
        exc = sys.exc_info()
        print(getattr(exc[0], '__name__', None), exc[1], sep=':\n\n  ')
        input('回车以退出... ')
        sys.exit(-1)
