.. _pnpiroot:

=================
Pinandpi 模块总述
=================

--------
pinandpi
--------

.. automodule:: pinandpi
   :members:
   :no-undoc-members:
   :platform: Windows

---
src
---

详细信息: :doc:`mod-src`

.. automodule:: pinandpi.src
   :noindex:
   :platform: Windows

-------
imagine
-------

详细信息: :doc:`mod-img`

.. module:: pinandpi.imagine
   :noindex:
   :platform: Windows


   提供布丰投针的算法.

   .. versionadded:: 1.1

   .. function:: throw(x=10**6)
      :noindex:

      见 :func:`pinandpi.alg_throw`

   .. function:: test()
      :noindex:

      见 :func:`pinandpi.alg_test`

   纯 Python 版本的算法:

   - old_algo()
   - old_throw(x=10**6)
   - old_test()

------
config
------

详细信息: :doc:`mod-cfg`

.. module:: pinandpi.config
   :noindex:
   :platform: Windows

   布丰投针 - 设置

   读取、修改设置, 修改将反映到主程序中.

   设置条目有:

   - **size**: {7, 8, 9, 10, 11, 12}, default 9
   - **theme**: {'light', 'dark'}
   - **language**: {'zh-hans', 'english'}
   - **using_matplotlib**: {'yes', 'no'}
   - **using_matplotlib**: {'yes', 'no'}
