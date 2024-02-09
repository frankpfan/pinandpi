==========
关于此文档
==========

这是 PynAndPi |release| 的文档。

.. note::
   这是一个脚注比正文长的页面，因为它本身就是用来放注释和链接的。

本文档使用 Sphinx [1]_ 从：

- Docutils [2]_ 的 reStructuredText [3]_ (.rst)；
- MyST [4]_ 的 Markdown [5]_ (.md)

生成，使用 PyData [#]_ 的 pydata-sphinx-theme [#]_ 主题。

作者: 樊圃 FAN Pu [#]_


.. rubric:: footnotes

.. [1]

Sphinx，Python 的第三方库，是生成文档的工具，但是也可以用来编写书籍，
不只在 Python 圈里有应用。

- **Site**: https://www.sphinx-doc.org/en/master/ （当然这个网站的内容是 Sphinx 自己生成的）

----------------

.. [2]

Docutils，Python 的第三方库，顾名思义，是一个文档工具。

- **Document**: https://docutils.sourceforge.io （当然这个页面也是 Docutils 自己生成的）
- **PyPI**: https://pypi.org/project/docutils

----------------

.. [3]

reStructuredText，简称 reST 或 rst，Python “御用” 文档语言。
是一种标记语言，功能较 Markdown 齐全，但是可读性稍低。
目前只有 Docutils 一种标准，但是可以轻松扩展，因此统一性强，可扩展性好。

.. centered:: "reStructuredText" is ONE word, not two!

- **Document**: https://docutils.sourceforge.io/rst.html （当然这个也是 Docutils 生成的）

----------------

.. [4]

MyST-Parser(Markedly Structured Text - Parser)，一个基于 CommomMark 标准上
扩展的 Docutils 和 Sphinx 扩展。

- **GitHub**: https://github.com/ExecutableBookProject/MyST-Parser
- **Document**: https://myst-parser.readthedocs.io/en/latest/ 

----------------

.. [5]

Markdown，也是一种文档标记语言，语法简洁。各家工具标准不一是它的最大缺点，
换工具还得改语法，只有基本语法是不变的，但是基本语法也会有个别变体……
所以这里不放链接了。

----------------

.. [#]

PyData，"A community for developers and users of open source data tools"，
像 `numpy`_, `scipy`_, `pandas`_, `matplotlib`_, `jupyter`_ 等都是其成员。

- **Site**: https://pydata.org/

----------------

.. [#]

PyData Sphinx Theme，PyData 社区很多文档都使用这个主题。
不是 Sphinx 的内置主题，需要下载（它是 Python 第三方库）。

- **Document**: https://pydata-sphinx-theme.readthedocs.io/en/stable/
- **PyPI**: https://pypi.org/project/pydata-sphinx-theme

----------------

.. [#]

樊圃，就是我…… 没得可介绍，放个 :doc:`空头链接 <update>` 凑数。

.. _numpy: https://numpy.org
.. _scipy: https://scipy.org
.. _pandas: https://pandas.pydata.org
.. _matplotlib: https://matplotlib.org
.. _jupyter: https://jupyter.org
