# &nbsp; 布丰投针：证明与算法

<div style="text-align: center;">

![PynAndPi Icon](f_icon.png 'PynAndPi Icon')

</div>

>
> > 作者：樊圃
>

## &nbsp; 0x00：证明

### &nbsp; &nbsp; 0b00：背景

> 法国数学家布丰（1707-1788）最早设计了投针试验.
> 这一实验的步骤是:
> 1. 取一张白纸, 在上面画上许多条间距为a的平行线.
> 2. 取一根长度为 $$l(l \le a)$$ 的, 随机地向画有平行直线的纸上掷 $$n$$次,
    观察针与直线相交的次数, 
    记为 $$i$$.
> 3. 计算针与直线相交的概率.

 "投针问题" 记载于布丰1777年出版的著作中: "在平面上画有一组间距为
 $$a$$ 的平行线, 
将一根长度为 $$l(l \le a)$$ 的针任意掷在这个平面上, 
求此针与平行线中任一条相交的概率. "

这里, 我们取 $$l=1, a=2$$.

### &nbsp; &nbsp; 0b01：证明

我们只考虑一根线的情况.
<del>（想知道它为什么可以等价与无穷多根平行线, 就自己证明. ）</del>
针的一端到线的距离 $$y$$ 的取值范围是 $$(-1, 1\,]$$ ,
针与线的夹角 $$\theta$$ 的取值范围是 $$[\,0, 2\pi)$$ .

考虑样本空间 $$\mathbf{S}=\{每一根可能的针\}$$ , 事件
$$\mathbf{A}=\{与线相交的针\}$$ , 随机变量

\$$
X =
\begin\{cases}
    1, \& \text{相交} \\\\
    0, \& \text{不相交}
\end\{cases}
\$$

不难看出, 当

\$$y - \sin\theta \le 0$$

时, $$X=1$$.

因此, 当 $$\theta=t_0$$ 时, $$X=1 \iff |y|<|\sin t_0|$$.

故事件 $$\mathbf{A}$$ 即 $${X=1}$$ 在 $$(y, \theta)$$ 坐标系中的图形是
$$y=\sin \theta$$ 与 $$\theta$$ 轴围成的图形.

这个图形的面积是：

\$$
\begin\{align}
    \int_0^{2\pi}\\!|\sin x|\mathrm\{d}x
    \& = 4\\!\int_0^{\pi/2}\\!\sin x\mathrm\{d}x \\\\
    \& = 4\left[-\cos x \right]_0^{\pi/2} \\\\ \\\\
    \& = 4\times[0-(-1)] \\\\ \\\\
    \& = 4
\end\{align}
\$$

而整个样本空间 $$\mathbf{S}$$ 的面积为 $$2 \times 2\pi = 4\pi$$,
所以投中概率为 $$\cfrac{4}{4\pi}=\cfrac{1}{pi}$$, $$X \sim B(1, \cfrac{1}{pi})$$,
所以当投针次数 $$n$$ 变大时, $$n/i$$ 不断接近 $$\pi$$.
（根据棣莫弗－拉普拉斯定理. ）

## &nbsp; 0x01：算法

在讲算法时应声明，布丰投针的模拟中是可以用到 $$\pi$$ 表示
$$\theta$$ 的，因为现实中的角度并不涉及 $$\pi$$，这里使用是为了
sin 函数的计算需要。

事实上，存在这样的随机算法，使得结果 $$\Delta y = \sin\theta$$
在 -1 与 1 之间且 $$D=\Delta y$$ 的概率密度正确，
但是一般来说这是没有必要的。

以下算法测试时的 CPU 占用均为约 9%（Python 3.10; Windows 10;
    Intel(R) Core(TM) i5-10400 CPU @ 2.90GHz）

### &nbsp; &nbsp; 0b00：Python 算法

纯 Python 实现的算法，使用 math 模块的 sin(), radians() 函数和 pi。

- [x] 不需要任何第三方包，原生 Python 即可实现。
- [ ] 速度慢，测试时投针 1 亿次需四十余秒。

### &nbsp; &nbsp; 0b01：Numpy 算法

- [x] 速度快，测试时投针 1 亿次仅需 3.2 秒左右。
- [ ] 需要安装 Numpy；内存占用大，上述速度需要 23MB 内存。
    优化前内存占用甚至是其 10 倍。

用 Python 的第三方包 Numpy 实现的算法。

```Python
# part of \pinandpi\imagine\algr_np.py
import numpy as np


rng = np.random.default_rng()

def th(x=100_0000):    #  1*10^8 needles, 9% of i5 cpu: 3.2s, ~23MB memory
    y_arr = rng.uniform(0., 2., (x,))
    dy_arr = np.sin(rng.uniform(0., np.pi, (x,)))
    b_arr = (y_arr - dy_arr) <= 0
    return x, np.sum(b_arr, dtype='i8')
```
使用：
```Python
>>> n = i = 0
>>> dn, di = th()
>>> n += dn
>>> i += di
>>> print(n, i, n/i)
<n> <i> <a-number-close-to-pi>
```

作者曾经（没事闲的）使用此算法进行几小时的实验，总计 *8192 亿*
根针，投中 2607,5985,1100 根，计算结果与 $$\pi$$ 真值相差
0.00015%（比真值小），而数学上预期误差应在约 0.00011% 内。推断为浮点误差，不可避免。


未来，我打算将 Numpy 算法加入主程序，并最终 **强制使用** Numpy。

<br />

<script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-svg.js">
</script>