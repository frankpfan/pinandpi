"""
布丰投针 - 读取记录

读取历史记录并返回. 调用 :func:`get()` 函数.
"""

import numpy as np


REC_FILE = 'history.txt'


def get():
    """
    以 :obj:`np.ndarray[typing.Any, np.dtype[np.int64]]`
    类型返回所有记录.

    Returns
    -------
    np.ndarray
        包含记录的数组.

    Note
    ----
    返回数组具有 shape `(-1, 3)`, 数据类型是 :obj:`np.uint64`.
    """
    return np.loadtxt(
        REC_FILE,
        encoding='utf-8',
        dtype=np.uint64,
        delimiter=',',
    )


if __name__ == '__main__':
    arr = get()
    print(repr(arr))
    print(repr((arr[:, 1] / arr[:, 2]).reshape((-1, 1))))
