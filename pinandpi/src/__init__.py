'''
源码包. 提供主程序、设置及记录读取.

以下为子模块：

* run
    主程序模块. 调用 :func:`~run.main()` 以运行.

* config
    设置模块, 调用 :func:`~config.main()` 以运行.

* readhistory
    读取历史记录并返回.
'''

from . import run
from . import config
from . import readhistory
