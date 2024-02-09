# &nbsp; &nbsp; 布丰投针：Python GUI 编程模拟

<div style="text-align: center;">

![PynAndPi Icon](f_icon.png 'PynAndPi Icon')

</div>

>
> > 作者：樊圃
> > 
> > 版本号：v1.1.0a
> > 
> > tips: 建议认真读完！
>

## &nbsp; &nbsp; 0x00：文件结构


&nbsp; &nbsp; *以下为文件结构树。*


```
   PynAndPi/
       基本文件夹，pyn 与 pin 形似，意为针，其中 py 代表 Python，pi 即 π，圆周率。
       |
       |- 使用说明.html  - 文档：即本文件。
       |- 原理解释.html  - 文档：证明及算法
       |- icon.png       - 图片：自制图标
       |
       |- main.pyw       - 运行入口
       |
       +- photos/        - 图片：PNG、ICON，我的图标。
       +- pinandpi/
           一个 Python 包（package），
           可以单独放到 PYTHON/Lib/site-packages 中，
           用 'import pinandpi; pinandpi.main()' 运行。
           |
           |- __init__.py    - Python 包的根本
           |
           +- imagine/       - 算法包
           |
           +- src/                
               源码文件夹
               |- __init__.py    - Python 包的根本
               |
               |- history.csv    - 与 src 内程序关联的历史记录文件。
               |- config.ini     - 配置文件，INI 格式
               |
               |- 使用说明.html  - 文档：也即本文件
               |- 原理解释.html  - 文档：证明及算法
               |
               |- config.py      - 配置程序
               |- run.py         - 主程序文件
               |
               +- photos/        - 图片：PNG、ICON，我的图标。
```



## &nbsp; &nbsp; 0x01：打开方式

- 点击 `main.pyw` 运行。

> New in 1.0.1:
> >此版本可以直接运行，也可作为 **`Python`** 模块（包）使用，
> >作为模块时请将 `pinandpy 文件夹` 放入``PYTHON/Lib/site-packages 文件夹``中。
> >（但是一个单体 GUI 程序也不需要被 import 呵呵  :-)）
> >
> >【如果作为模块（包），不传到 [**`PyPI`**](https://pypi.org) 上就是可惜了！可是我不会…… 】

## &nbsp; &nbsp; 0x02：程序特点

<br />

&nbsp;&nbsp; 使用 [**`Python(CPython)`**](https://www.python.org) 编写，没有命令行窗口，
只有使用 [**`tkinter`**](https://docs.python.org/zh-cn/3/library/tkinter.html) 自制的 `GUI` 界面。

注：

- 若使用`.pyw`文件**双击运行**，则没有命令行窗口；
- 若将扩展名改为 `.py`，则会有命令行窗口；
- 在 **`IDLE Edit Window`** 中运行，则有 IDLE 交互界面。

&nbsp; &nbsp; 界面力求**简洁大方**，希望大家喜欢 :D


## &nbsp;&nbsp; 0x03：程序“玩法”

```Python
   pass    # Python 关键字，什么也不做，占位用。
```
开个玩笑哈哈。 ;)

1. 点击 **`开始投针`**；
2. 在`控制区`选择模式：
    - 持续模式会一直投针，若不画新针则每 500,0000 根针刷新一次π值；
    - 非持续模式可以选择每次投的针数，也有画针/不画针的区分。
    - 按钮变为淡蓝色即为开启，白色为关闭。

    按 **`重新开始`** 会清零当前进度。
3. 
    + 在`功能区`有开始按钮和选择投针数的按钮。投针期间开始按钮会变成停止，且其他按钮不能用。

    + **`历史记录`**中，可以选取历史记录，也可以保存进度，还有依靠 **`matplotlib`** 的记录分析。
    [**`matplotlib`**](https://matplotlib.org 'matplotlib官网')
    是 Python 的第三方包（跟数学有关的总离不了 [`numpy`](https://numpy.org 'numpy官网'), `matplotlib`,
        [`pandas`](https://pandas.pydata.org)）,
    需要下载安装。
    在命令行中：
        ```
        .> python3 -m pip install --upgrade numpy
        .> python3 -m pip install --upgrade matplotlib
        ```
        然后，等待下载完成，在 **Python** 中：
        ```Python
        import matplotlib
        ```
        没有报错就行！ :-)

## &nbsp;&nbsp; 0x04：注意事项

&nbsp;&nbsp; 尽量不要改动任何文件，可以改变的是 `config.ini`，即设置文件。

> New in 1.1.0:
> > 现在，如果用户写入的设置有异常，运行 `config.py` 可以写回正确数据。
> >

## &nbsp; &nbsp; 0x05：证明及算法

&nbsp;&nbsp; 见 [*文档：证明与算法*](int.html),
这可能需要读者有一定的微积分、概率论基础（我是怎么会的就不要问了
    :stuck_out_tongue_winking_eye:）

<br />

<div style="background:#ddd">

<br />

<small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
本文档使用 **`Visual Studio 2022`**
中的 `Markdown` 插件写成并转为 `html` 文件。
</small>

<br />

</div>
