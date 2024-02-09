'''
提供布丰投针的算法.

.. versionadded:: 1.1

Functions
---------
.. function:: throw(x=10**6)
   :noindex:

   见 :func:`pinandpi.alg_throw`

.. _imgftest:

.. function:: test()
   :noindex:

   见 :func:`pinandpi.alg_test`

.. function:: old_algo()

   纯 Python 算法的判定函数.

.. function:: old_throw(x=10**6)

   纯 Python 算法的投针函数.

.. function:: old_test()

   纯 Python 算法的测试函数, 与 :ref:`test() <imgftest>` 的不同是,
   由于速度较慢, 它每 1000,0000 次输出一次.
'''

from .algorithm12 import im as old_algo
from .algorithm12 import th as old_throw
from .algorithm12 import main as old_test
from .algorithm22 import th as throw
from .algorithm22 import main as test


__all__ = [
    # Python + numpy
    'throw',
    'test',
    # pure Python
    'old_algo',
    'old_throw',
    'old_test',
]
