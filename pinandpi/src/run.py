"""
布丰投针 Python GUI 编程模拟

提供一个图形化的布丰投针界面.
"""

from collections import deque
from datetime import datetime
from math import sin, cos, radians
from random import uniform
from time import sleep, time
from tkinter import ttk
import decimal as dec
import os
import threading
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser as wb

import numpy as np

# version := major + minor + micro + state
major = 1  # major := int8 major version
minor = 2  # minor := int8 minor version
micro = 3  # micro := int8 micro version
state = 'a1'  # state := (a | b | f) + int4 level

# compute hexversion & version
version_tree = major, minor, micro
hexversion = hv = sum(
    [version_tree[2 - i] << (i + 1) * 8 for i in range(3)],
    start=int(state, base=16),
)
version = __version__ = '.'.join([str(v) for v in version_tree]) + state

del major, minor, micro, state, version_tree

BASEDIR = os.path.dirname(os.path.abspath(__file__))
BASEDIR = BASEDIR.replace('/', '\\').rstrip('\\') + '\\'

# ############################## data ############################## #

# 设置参数: 所有常量 #

# 绘图基本设置
NEEDLE_LEN = 36  # 针长(pixels)
LINE_DIS = NEEDLE_LEN * 2  # 线间距(pixels)

# 屏幕设置
CANV_H = LINE_DIS * 9  # 投针区高
CANV_W = CANV_H + 5  # 投针区宽

PI_W = CANV_W + 10

CTRL_H = CANV_H + 40  # 控制区高
CTRL_W = 150

SCREEN_H = CANV_H + 40  # 窗口总高
SCREEN_W = CANV_W + CTRL_W  # 窗口总宽
SCREEN_SIZE = SCREEN_W, SCREEN_H  # 窗口宽高元组

# 颜色
HOME_BG = '#5ad'  # 首页背景
TITLE_FG = '#147'  # 首页标题颜色

HOME_BUTTON_COLOR = '#4169e1'  # 首页按钮底色
HOME_BUTTON_ACTIVE_COLOR = '#527ad2'  # 首页按钮按下时颜色
HOME_BUTTON_TEXT_COLOR = '#e0eeff'  # 首页按钮字体颜色

GAME_BG = '#fffffa'  # 游戏界面背景

# 详细信息
INFO = '''
作者：Frank FAN

名称：布丰投针：Python GUI 编程模拟
又称“Pyn and Pi”。

提供一个图形化的布丰投针界面

版本号：1.2.2
'''


# -*- tkinter functions -*- #####


def windowplace(win, ww, wh):
    """
    将窗口放置在屏幕给定位置.

    Parameters
    ----------
    win: tk.Tk or tk.Toplevel
        要放置的窗口.

    ww, wh: int
        窗口的长宽.
    """
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('{:d}x{:d}+{:d}+{:d}'.format(
        ww, wh,
        (sw - ww) // 2, (sh - wh) // 2 - 20,
    ))


def widthof(widget):
    return widget.winfo_reqwidth()


def heightof(widget):
    return widget.winfo_reqheight()


def xmiddleplace(widget, master_w, ypos=0):
    """
    将控件放置在屏幕横向中央位置.

    Parameters
    ----------
    widget: tk.Widget
        要放置的控件.

    master_w: int
        父控件宽.

    ypos: int = 0
        y 轴位置.
    """
    wid_w = widthof(widget)
    x_middle = (master_w - wid_w) // 2
    widget.place(x=x_middle, y=ypos)


# ############################## imgn ############################## #

rng = np.random.default_rng()


def imalthrow(y, d):  # 效率声明： 100,0000次, 1.1685秒.
    dy = NEEDLE_LEN * sin(radians(d))
    home.game.needles += 1
    if (y - NEEDLE_LEN) % LINE_DIS == 0:
        home.game.intersected += 1
    elif dy != 0:
        lineno = (y - NEEDLE_LEN) // LINE_DIS
        lineno2 = (y + dy - NEEDLE_LEN) // LINE_DIS
        if lineno != lineno2:
            home.game.intersected += 1


def npthrow(x=10 ** 6):  # 效率声明：1*10^8 次, 3.2s, ~130MB 内存
    y_arr = rng.uniform(0., 2., (x,))
    dy_arr = np.sin(rng.uniform(0., np.pi, (x,)))
    b_arr = (y_arr - dy_arr) <= 0
    return x, np.sum(b_arr, dtype='i8')


def imrdthrow(n):  # 效率声明： 100,0000次, 2.0932秒.
    if n == -1:
        while home.game.throwing:
            for _ in range(500000):
                imalthrow(uniform(0, CANV_H),
                          uniform(0, 360))
            home.game.update_pi(home.game.intersected, home.game.needles)
    else:
        for _ in range(n):
            if home.game.throwing:
                imalthrow(uniform(0, CANV_H), uniform(0, 360))
    home.game.throwing = False
    home.game.update_pi(home.game.intersected, home.game.needles)
    home.game.start_b['text'] = ' 投    针 '
    for w in home.game.other_b:
        w.config(state='normal')
    home.game.update_rbuttons_states()


def imthrow(n=1000):
    for w in (*home.game.other_b, *home.game.radiobuttons):
        w.config(state='disabled')
    t = threading.Thread(target=imrdthrow, args=(n,), daemon=True)
    t.start()


# ############################## recd ############################## #

MAX_PIECES = 15
MAX_LOGS = 1000
REC_FILE = os.path.join(BASEDIR, 'history.txt')


def _datefmt(ts):
    time_msg = datetime.strftime(datetime.fromtimestamp(ts),
                                 '%Y/%m/%d %H:%M:%S')
    return time_msg


def iofunc(func):  # decorator
    """
    为文件操作提供的安全性装饰器.

    Parameters
    ----------
    func: Callable
        要调用的函数.

    Returns
    -------
    inner(*args, **kw): function
        尝试执行 :guilabel:`func(*args, **kw)`, 若捕获到 :exc:`PermissionError`
        则提示关闭文件.
    """

    def inner(*args, **kw):
        try:
            r = func(*args, **kw)
        except PermissionError:  # 似乎不会发生, 但是以防万一
            msgbox.showerror(
                '布丰投针：文件操作错误',
                '请检查 {} 是否关闭！'.format(REC_FILE)
            )
        else:
            return r

    return inner


@iofunc
def record(a, b):
    if a < 128:
        msgbox.showwarning(
            '布丰投针 - 历史记录',
            '投针次数太少，请仅保存投针至少 128 次的记录！',
        )
        return False  # 保存失败
    t = int(time())
    msg = '{:d}, {:d}, {:d}\n'.format(t, a, b)
    with open(REC_FILE, 'a', encoding='utf-8') as f:
        f.write(msg)
    return True  # 保存成功


@iofunc
def get(max_size=None):
    """
    以 :type:`np.ndarray[typing.Any, np.dtype[np.int64]]`
    类型返回一定数目的记录.

    Parameters
    ----------
    maxsize: int or None
        最多返回的记录数. 若为 `None`, 返回所有记录.

    Returns
    -------
    np.ndarray
        包含记录的数组.

    Note
    ----
    返回数组具有 shape `(-1, 3)`, 数据类型是 :type:`np.uint64`.
    """
    res = np.loadtxt(
        REC_FILE, encoding='utf-8',
        dtype=np.uint64, delimiter=', '
    )
    if max_size is not None:
        return res[:-max_size - 1:-1]
    return res


class Record:
    """历史记录模块操作."""

    def __init__(self, game):
        """
        初始化 :class:`Record`.

        Parameters
        ----------
        game: Game
            使用 :obj:`self` 的 :class:`Game` 对象.
        """
        self.game = game
        self.c_win = None

    def leave(self):
        """离开历史记录界面."""
        self.showing = False
        self.game.win.attributes('-disabled', 0)
        self.c_win.destroy()
        self.game.win.focus_force()

    def search_win(self):
        """读取记录."""
        self.game.win.attributes('-disabled', 1)
        self.c_win.destroy()
        win = tk.Toplevel(self.game.win)

        win.title('记录导入')
        win['bg'] = '#3366ee'
        win.protocol('WM_DELETE_WINDOW', self.leave)
        win.focus_force()

        msgs = get(MAX_PIECES)
        options = [', '.join([_datefmt(t), str(a), str(b)])
                   for t, a, b in msgs]
        lb = tk.Listbox(
            win, bg='#f3f5ff', fg='#111122',
            font=('Courier',),
            width=max([len(x) for x in options] + [56]),
            height=MAX_PIECES,
        )
        if not options:
            lb.insert('end', ' -*-#- 无记录 -#-*- ')
        else:
            for text in options:
                lb.insert('end', text)
        lb.place(x=8, y=8)

        width = lb.winfo_reqwidth()
        lbheight = lb.winfo_reqheight()
        windowplace(win, width + 16, lbheight + 130)

        def load():  # bad code smell
            if not options or not lb.curselection():
                return
            frac = msgs[lb.curselection()[0], 1:]
            self.leave()
            self.game.intersected = int(frac[1])
            self.game.needles = int(frac[0])
            self.game.update_pi(*map(int, frac[[1, 0]]))

        b1 = tk.Button(win, text='确  定', command=load)
        b1.place(y=lbheight + 28, x=width // 2 - 45, width=90, height=35)

        b2 = tk.Button(
            win, text='返  回',
            command=lambda: [win.destroy(), self.record_win(strict=False)],
        )
        b2.place(y=lbheight + 80, x=width // 2 - 45, width=90, height=35)

        win.transient(self.game.win)
        self.c_win = win
        self.showing = True
        win.lift()
        win.focus_force()

    # ! matplotlib interface ! #

    def mpl_part(self):
        """历史分析界面."""
        self.c_win.title('稍等……')
        try:
            import matplotlib.pyplot as plt
            from matplotlib.backends.backend_tkagg import \
                FigureCanvasTkAgg, NavigationToolbar2Tk
            import matplotlib.ticker as mpltck
            self.c_win.destroy()
        except ImportError:
            if msgbox.askyesnocancel(
                    '布丰投针 - matplotlib 下载提示',
                    '您未安装 matplotlib, 是否安装以使用分析功能？',
            ):
                self.c_win.focus_force()
                os.system('pip install matplotlib')
            self.c_win.title('历史记录操作')
            return

        infos = get()[:, 1:]  # infos:: [[投针次数, 投中次数]*]

        if len(infos) <= 12:
            msgbox.showinfo('布丰投针 - 统计提示',
                            '历史记录数据太少，可能不能得到很好的展示效果！')

        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # ! 处理数据
        # A.hist
        a_x = infos[:, 0]
        a_mean = a_x.mean()
        a_max = a_x.max()
        a_ticks = np.linspace(0, 10 ** np.ceil(np.log10(a_max)),
                              101, endpoint=True, dtype=int)

        # B.info
        b_num = len(infos)
        b_mean = infos[:, 0].sum() / infos[:, 1].sum()
        b_err = b_mean / np.pi - 1

        # C.scatter
        c_x = infos[:, 0]
        c_y = c_x / infos[:, 1] / np.pi
        c_u = c_y > 1
        c_l = c_y <= 1
        c_a = [(x, y) for x, y in zip(c_x[c_u], c_y[c_u])]
        c_b = [(x, y) for x, y in zip(c_x[c_l], c_y[c_l])]
        c_a.sort()
        c_b.sort()
        c_a = list(zip(*c_a))
        c_b = list(zip(*c_b))

        # ! 分割图像区域
        fig = plt.figure(figsize=(9, 6))  # figsize:: (inch, inch)

        root = tk.Toplevel(self.game.win)
        root.title('布丰投针 - 历史分析')
        root.attributes('-fullscreen', True)
        root.protocol('WM_DELETE_WINDOW', self.leave)

        self.c_win = root
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)

        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        axA = fig.add_subplot(2, 2, 1)
        axB = fig.add_subplot(2, 2, 2)
        axC = fig.add_subplot(2, 2, (3, 4))

        # ! plot.

        # A.hist
        axA.set_title('投针次数统计直方图')  # title
        axA.xaxis.set_major_locator(mpltck.FixedLocator(a_ticks))  # `x` axis
        axA.set_xticklabels(['{:,g}'.format(x) for x in a_ticks],
                            rotation=40, ha='right', va='top')
        axA.set_xlim(100, a_max * 1.05)
        a_ylim = axA.hist(a_x, alpha=0.6, color='r')[0].max()  # histogram
        axA.set_ylim(0, a_ylim + 1)  # `y` axis
        axA.grid(linestyle='--', alpha=0.3)  # grid
        # A.line
        axA.plot([a_mean, a_mean], axA.set_ylim(), color='orange',  # \mu mean
                 linestyle='-', alpha=0.8, label=r'$\mu$ 平均值')
        axA.annotate(r'$\quad\mu={:.3f}$'.format(a_mean),
                     xy=[a_mean, axA.set_ylim()[1] * 0.95],
                     color='#00d')
        axA.fill_between([axA.set_xlim()[0], a_mean], axA.set_ylim()[1],
                         color='orange', alpha=0.1)
        axA.legend()
        axA.spines['top'].set_visible(False)
        axA.spines['right'].set_visible(False)

        # B.info
        infotext = (
            '记录数       ：{}\n'
            '总 $\\pi$ 值      ：{:.15f}\n'
            '平均投针次数 ：{:.5f}\n'
            '总误差       ：{:%}'
        ).format(b_num, b_mean, a_mean, b_err)
        for sp in axB.spines.values():
            sp.set_visible(False)
        axB.set_xticks([])
        axB.set_yticks([])
        axB.text(s=infotext, x=0.05, y=0.5,
                 ha='left', va='center', fontsize=14)

        # C.scatter
        axC.set_xscale('log')
        axC.set_yscale('log')
        axC.plot(*c_a, color='b', alpha=0.3)
        axC.plot(*c_b, color='r', alpha=0.3)
        axC.scatter(c_a[0], c_a[1], color='b', alpha=0.6, label=r'$y>0$')
        axC.scatter(c_b[0], c_b[1], color='r', alpha=0.6, label=r'$y<0$')
        axC.plot(axC.set_xlim(), (1, 1), color='k', linestyle='-.', alpha=0.25)
        axC.set_xlim(c_x.min() * 0.5, c_x.max() * 2)
        axC.set_ylim(c_y.min() * 0.75, c_y.max() * 1.25)
        axC.grid(which='both', axis='x', linestyle='-.', color='k', alpha=0.2)
        axC.set_xlabel(r'$x =$ 投针次数')
        axC.set_ylabel(r'$y = {\overline{p} / \pi}$')
        axC.legend()

        # todo 布局+显示
        plt.tight_layout()
        canvas.draw()
        toolbar.update()

        def quit_func():
            fig.clf()
            plt.close()
            self.leave()

        quit_b = tk.Button(
            root, text='返    回', height=1,
            command=quit_func,
            bg='#78a', fg='#eef', relief='flat',
            font=(None, 12, 'bold'),
        )
        quit_b.pack(side=tk.BOTTOM, fill=tk.X)

        root.protocol('WM_DELETE_WINDOW', quit_func)

        root.transient(self.game.win)
        root.focus_force()

    # ! end mpl interface ! #

    showing = False
    last_saving_time = 0

    def record_win(self, strict=True):
        if strict and self.showing:
            return
        self.game.win.attributes('-disabled', 1)

        win = tk.Toplevel(self.game.win)
        windowplace(win, 240, 260)
        win.title('历史记录操作')
        win['bg'] = '#3366ee'
        win.focus_force()
        win.protocol('WM_DELETE_WINDOW', self.leave)

        b1 = tk.Button(
            win, text='读取·记录', font=('宋体', 11, 'bold'),
            bg='#66ccff', activebackground='#77ccff',
            command=self.search_win,
        )
        b2 = tk.Button(
            win, text='保存·进度', font=('宋体', 11, 'bold'),
            bg='#66ccff', activebackground='#77ccff',
            command=lambda: (     # bad code flavour
                abs(time() - Record.last_saving_time) > 12 and [
                    setattr(self, 'lastsavetime', time()),
                    record(self.game.needles, self.game.intersected) and [
                        self.leave(),
                        msgbox.showinfo(
                            '布丰投针',
                            '进度保存成功！',
                        ),
                    ],
                ] or [
                    msgbox.showerror(
                        '布丰投针',
                        '两次保存请隔 12 秒以上!',
                    ),
                    self.leave(),
                    self.game.win.attributes('-disabled', 0),
                ],
            ),
        )
        b3 = tk.Button(
            win, text='历史·分析', font=('宋体', 11, 'bold'),
            bg='#66ccff', activebackground='#77ccff',
            command=self.mpl_part
        )
        b4 = tk.Button(
            win, text=' 返·回 ', font=('宋体', 11, 'bold'),
            bg='#66ccff', activebackground='#77ccff',
            command=self.leave
        )

        b1.place(x=60, y=22, width=120, height=36)
        b2.place(x=60, y=82, width=120, height=36)
        b3.place(x=60, y=142, width=120, height=36)
        b4.place(x=60, y=202, width=120, height=36)

        win.transient(self.game.win)
        self.c_win = win
        self.showing = True


# ############################## game ############################## #


def gen_color():
    """
    生成画下针的颜色.

    Yields
    ------
    color: :obj:`str`, regex :regex:`#(\\d{2}){3}`
         颜色, 由 '#ff0000' 开始, 至 '#00ff00', 再到 '#0000ff', 循环.
    """
    r, g, b = 255, 0, 0
    yield '#ff0000'
    dr, dg, db = -1, 1, 0
    while True:
        for _ in range(255):
            r += dr
            g += dg
            b += db
            yield '#%02x%02x%02x' % (r, g, b)
        dr, dg, db = db, dr, dg


class Game:
    """投针界面."""

    def __init__(self, home):
        """
        初始化 :class:`Game`.

        Parameters
        ----------
        home: Home
            使用 :obj:`self` 的 :class:`Home` 对象.
        """
        self.home = home

        self.lineids = deque()
        self.needles = 0
        self.intersected = 0

        self.n_once = tk.IntVar()
        self.n_once.set(1)

        self.showing = True
        self.throwing = False

        self.mode = 1  # 0持续, 1手动
        self.draw = 1  # 0不画, 1画针
        self.color_gen = gen_color()

        self.needles = 0
        self.intersected = 0

        self.record = Record(self)

    # 交接工作 #

    def destroy_home(self):
        if self.home.showing:
            self.home.win.destroy()
            self.home.showing = False

    def back2home(self):
        if self.showing:
            self.win.destroy()
            self.showing = False
            self.home.show()

    # -*- 主题 -*- #

    def throw(self, x, y, d):
        cv = self.canvas
        dx = NEEDLE_LEN * cos(radians(d))  # math
        dy = NEEDLE_LEN * sin(radians(d))  # math
        self.lineids.append(
            cv.create_line(
                x, y,
                x + dx, y + dy,
                fill=self.color_gen.__next__(),
            ),
        )
        self.needles += 1
        if len(self.lineids) >= 220:  # 画布上的针数上限
            cv.delete(self.lineids.popleft())

        if (y - NEEDLE_LEN) % LINE_DIS == 0:
            self.intersected += 1
        elif dy != 0:
            lineno = (y - NEEDLE_LEN) // LINE_DIS
            lineno2 = (y + dy - NEEDLE_LEN) // LINE_DIS
            if lineno != lineno2:
                self.intersected += 1
        self.update_pi(self.intersected, self.needles)
        self.win.update_idletasks()

    def throw_once(self):
        self.throw(
            uniform(0, CANV_H),  # math
            uniform(0, CANV_H),  # math
            uniform(0, 360),  # math
        )

    def randthrow(self, n, delay=0):
        if n == -1:
            while self.throwing:
                self.throw_once()
        else:
            for _ in range(n):
                if self.throwing:
                    self.throw_once()
                    sleep(delay)
        self.throwing = False
        self.start_b['text'] = ' 投    针 '
        for w in self.other_b:
            w.config(state='normal')
        self.update_rbuttons_states()

    def thrdthrow(self, n):
        for w in (*self.other_b, *self.radiobuttons):
            w.config(state='disabled')
        t = threading.Thread(
            target=self.randthrow,
            args=(
                n,
                0 < n <= 10 and 0.05
                or (0 < n <= 100 and 0.02 or 0)
            ),
            daemon=True,
        )
        t.start()

    def update_rbuttons_states(self):
        if self.mode:
            if self.draw:
                states = [1] * 5 + [0] * 2
            else:
                states = [1] * 7
        else:
            states = [0] * 7
        for w, s in zip(self.radiobuttons, states):
            w['state'] = s and 'normal' or 'disabled'

    def _title_process(self):
        n = 0
        while self.throwing:
            yield self.win.title(' Python 布丰投针 - 投针中' + ' #' * n)
            sleep(0.2)
            n = n % 8 + 1
        return self.win.title(' Python 布丰投针')

    def title_process(self):
        """
        窗口标题进度条.

        投针时在标题中添加 ' #', 至 8 个重新开始.
        """
        t = threading.Thread(
            target=lambda *args: list(args),
            args=self._title_process(), daemon=True
        )
        t.start()

    def start_b_cmd(self):
        b = self.start_b
        self.throwing = False if b['text'] == ' 停    止 ' else True
        if self.throwing:
            b['text'] = ' 停    止 '
            if not self.mode:
                if self.draw:
                    self.thrdthrow(-1)
                else:
                    imthrow(-1)
            else:
                ((imthrow, self.thrdthrow)[self.draw])(self.n_once.get())
            self.title_process()
        else:
            b['text'] = ' 投    针 '

    def mode_b_cmd(self):
        b = self.other_b[0]  # 模式按钮是第一个
        if self.mode == 1:
            self.n_last = self.n_once.get()
            self.n_once.set(-1)
            b['bg'] = '#adf'
            self.mode = 0
        else:
            if self.draw == 1:
                self.n_once.set(min(self.n_last, 10000))
            else:
                self.n_once.set(self.n_last)
            b['bg'] = '#fffefe'
            self.mode = 1
        self.update_rbuttons_states()

    def draw_b_cmd(self):
        b = self.other_b[2]  # 第三个
        if self.draw == 1:
            b['bg'] = '#adf'
            self.draw = 0
            self.update_rbuttons_states()
            return
        self.n_once.set(min(self.n_once.get(), 10000))
        b['bg'] = '#fffefe'
        self.draw = 1
        self.update_rbuttons_states()

    def restart(self):
        self.needles = 0
        self.intersected = 0
        for n in self.lineids:
            self.canvas.delete(n)
        self.lineids.clear()
        self.update_pi(self.needles, self.intersected)

    def placewidgets(self, f):
        area_ctrl = tk.LabelFrame(f, text='控制区')
        f.add(area_ctrl, weight=8)
        area_mthd = tk.LabelFrame(f, text='功能区')
        f.add(area_mthd, weight=12)
        area_bye = tk.LabelFrame(f, text='Exit')
        f.add(area_bye, weight=6)

        b_style_dict = dict(width=12, background='#fcfefe',
                            activebackground='#f0f0f0', relief='ridge',
                            bd=2, highlightcolor='#eee')

        b1 = tk.Button(area_ctrl, text='持续模式?',
                       command=self.mode_b_cmd, **b_style_dict)
        b2 = tk.Button(area_ctrl, text='重新开始?',
                       command=self.restart, **b_style_dict)
        b3 = tk.Button(area_ctrl, text='不画新针?',
                       command=self.draw_b_cmd, **b_style_dict)

        b4 = tk.Button(area_mthd, text='历史记录',
                       command=lambda:
                       self.record.showing or self.record.record_win(),
                       **b_style_dict)
        b5 = tk.Button(
            area_mthd, text=' 投    针 ', command=self.start_b_cmd,
            **{**b_style_dict, 'fg': '#f00', 'background': '#fffdf5'},
        )
        self.start_b = b5

        # RadioButton 投针数选项：1, 10, 100, 1000, 10000, 100000, 1000000
        # 并且在画针模式下, 最后两个选项将无用, 若选中则自动跳到 1_0000.
        rbs = []
        for i in range(7):
            rbs.append(ttk.Radiobutton(
                area_mthd, text=10 ** i, value=10 ** i, variable=self.n_once,
                command=lambda x=10 ** i: self.n_once.set(x)))
        self.radiobuttons = rbs
        rbs[0].invoke()

        bL1 = tk.Button(area_bye, text='退    出',
                        command=self.leave, **b_style_dict)
        bL2 = tk.Button(area_bye, text='返回首页',
                        command=self.back2home, **b_style_dict)

        self.other_b = (b1, b2, b3, b4, bL1, bL2)

        # ! 放置

        b1.place(relx=0.5, rely=2 / 10, anchor='center', height=35)
        b2.place(relx=0.5, rely=5 / 10, anchor='center', height=35)
        b3.place(relx=0.5, rely=8 / 10, anchor='center', height=35)

        b4.place(relx=0.5, rely=2 / 14, anchor='center', height=35)
        b5.place(relx=0.5, rely=5 / 14, anchor='center', height=35)

        for i in range(7):
            rbs[i].place(relx=0.05, rely=(i + 7) / 14, anchor='w')
        for w in self.radiobuttons[-2:]:
            w.config(state='disabled')

        bL1.place(relx=0.5, rely=2 / 7, anchor='center', height=35)
        bL2.place(relx=0.5, rely=5 / 7, anchor='center', height=35)

    def update_pi(self, a, b):
        """
        更新画布下方显示的 :math:`\\pi` 值.

        Parameters
        ----------
        a: int
            投中次数.
        b: int
            投针次数.
        """
        dec.setcontext(dec.Context(prec=50))
        if a == 0:
            pi = float('NaN')
        else:
            pi = dec.Decimal(b) / dec.Decimal(a)
        self.pi_var.set(' π = {0: .48F}\n  ( {2} / {1} )'.format(pi, a, b))

    def leave(self):
        if msgbox.askokcancel('布丰投针：退出？', '确定要退出吗？'):
            self.win.destroy()
            self.win.quit()

    def show_game(self):
        self.destroy_home()

        win = tk.Tk()
        win.iconbitmap(
            tk.PhotoImage(os.path.join(BASEDIR, 'static\\p_icon.ico')),
        )
        windowplace(win, SCREEN_W, SCREEN_H)
        win.resizable(False, False)
        win['bg'] = GAME_BG

        win.focus_force()
        win.title(' —— 准备中 ……')

        cv = tk.Canvas(win, bg=GAME_BG,
                       highlightthickness=0, bd=0, takefocus=False)
        cv.place(x=5, y=0, height=CANV_H, width=CANV_W)

        pi_var = tk.StringVar()
        self.pi_var = pi_var
        self.update_pi(0, 0)

        self.pi_disp = tk.Label(
            win, bg='#dddddf', textvariable=pi_var, anchor='center',
            font=('Arial', 12, 'italic bold'), relief='groove',
            highlightcolor='#dca', highlightbackground='#dca', bd=3,
        )
        self.pi_disp.place(x=0, y=CANV_H, width=PI_W, height=40)

        self.style_paned = ttk.Style()
        self.style_paned.configure('TPanedwindow', relief='groove')
        self.ctrl1 = ttk.Panedwindow(win)  # sashwidth=0, handlesize=0)
        self.ctrl1.place(x=CANV_W + 5, y=0, width=CTRL_W, height=CTRL_H)
        self.placewidgets(self.ctrl1)

        self.win = win
        self.canvas = cv

        y = -NEEDLE_LEN
        for _ in range(9):
            sleep(0.12)
            y += LINE_DIS
            cv.create_line(0, y, CANV_W - 5, y)
            win.update()

        win.title(' Python 布丰投针')
        win.protocol('WM_DELETE_WINDOW', self.leave)

    def start(self):
        self.show_game()
        self.win.mainloop()


# ############################## home ############################## #

class Home:
    """首页界面."""

    def __init__(self):
        self.showing = False

    def topdesc(self):
        try:
            wb.open(os.path.join(BASEDIR, r'static\html\desc.html'), new=2)
        except Exception:
            msgbox.showerror('打开文件失败', '程序找不到介绍文件！')

    def topinterp(self):
        try:
            wb.open(os.path.join(BASEDIR, r'static\html\int.html'), new=2)
        except Exception:
            msgbox.showerror('打开文件失败', '程序找不到算法说明文件！')

    def topinfo(self):
        for w in home.win.children.keys():
            if w.startswith('!toplevel'):
                return
        top = tk.Toplevel(home.win, bg='#add')
        top.title('布丰投针 - 详细信息')
        windowplace(top, 400, 400)
        top.attributes('-alpha', 0.9)
        top.lift()
        top.focus_force()

        L = tk.Label(top, bg='#add', font=('宋体', 12, 'bold'), text=INFO)
        L.place(x=0, y=0, width=400, height=340)
        ok_b = tk.Button(
            top, text='Ok', command=top.destroy,
            bg='#acf', activebackground='#bdf', cursor='dotbox',
        )
        ok_b.place(x=160, y=350, width=80, height=30)
        top.transient(self.win)
        self.win.wait_window(top)

    def show(self):
        """主程序: 显示界面."""
        self.showing = True

        win = tk.Tk()
        self.win = win
        windowplace(win, 500, 280)
        win.maxsize(520, 300)
        win.minsize(480, 260)
        win.title('布丰投针 - 投出一个π')
        win['bg'] = HOME_BG

        title_L = tk.Label(win, text='布 丰 投 针',  # 主页标题
                           font=('微软雅黑', 67, 'bold'),
                           fg=TITLE_FG, bg=HOME_BG)
        self.home_L = title_L
        xmiddleplace(title_L, 500, 32)

        self.game = Game(self)
        texts = ['开始投针', '玩法介绍', '原理解释', '详细信息']
        buttons = []
        placesep = (500 - 52 - 95) / 3
        funcs = [self.game.start, self.topdesc, self.topinterp, self.topinfo]
        cursors = ['mouse', 'heart', 'sizing', 'target']
        btncfg = dict(
            bg=HOME_BUTTON_COLOR,
            activebackground=HOME_BUTTON_ACTIVE_COLOR,
            fg=HOME_BUTTON_TEXT_COLOR,
            activeforeground=HOME_BUTTON_TEXT_COLOR,
            font=('宋体', 11),
        )
        for i in range(4):
            buttons.append(tk.Button(win, text=texts[i], command=funcs[i],
                                     cursor=cursors[i], **btncfg))
            buttons[i].place(x=(26 + placesep * i), y=195, width=95, height=38)
        # 把按钮加入 Home
        self.buttons = buttons

        win.focus_force()
        win.lift()
        win.mainloop()


home = Home()
main = home.show

if __name__ == '__main__':
    home.show()
