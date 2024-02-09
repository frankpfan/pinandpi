'''
布丰投针 Python GUI 编程模拟

提供一个图形化的布丰投针界面，包括历史记录及数据分析.

:Version: 1.2.3a1
:Author: 樊圃 FAN Pu
:Platform: Windows

Functions
---------
.. function:: main()

    主程序入口.

.. function:: alg_throw(x=10**6)

    Numpy 算法.

    x: int = 10**6
        投针次数.

.. function:: alg_test()

    一个无限循环, 每次循环投针 2 亿次并输出总投针、投中次数及估算
    :math:`\\pi` 值.

.. seealso::
   :doc:`mod-img`

SubModules
----------

============================= ===================================
 名称                          说明
============================= ===================================
:mod:`~pinandpi.config`        设置模块.

:mod:`~pinandpi.imagine`       where **alg_*()** funcs are from.

:mod:`~pinandpi.run`           where function **main()** is from.
============================= ===================================
'''

from . import imagine
from .imagine import throw as alg_throw
from .imagine import test as algo_test
from .src import run, config, readhistory


__author__ = '樊圃 FAN Pu'
__version__ = version = run.version
hexversion = run.hexversion

main = run.main
