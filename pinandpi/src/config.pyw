"""
布丰投针 - 设置

读取、修改设置, 修改将反映到主程序中.

以下是设置条目:

size: {7, 8, 9, 10, 11, 12}, default 9
    | 投针界面大小. (Default 803x688)
    | 设置为 7 时, 窗口大小约 590x475;
      设置为 12 时, 窗口大小约 1020x904.
    | 实际上, 这在底层改变投针界面画布 (tk.Canvas) 的大小.

theme: {'light', 'dark'}
      投针界面的色调.

language: {'zh-hans', 'english'}
    .. attention::
       我没有实现, 也没有打算实现它.
       界面上的语言将永远是中文 ——
       即使包括 config.ini 在内的大部分文件都是英文的!

using_numpy: {'yes', 'no'}
    使用 Python 的第三方包 :mod:`numpy` 作算法.

    .. deprecated:: 1.3

using_matplotlib: {'yes', 'no'}
    使用 Python 的第三方包 :mod:`matplotlib`.
    它在 :menuselection:`开始投针 --> 历史记录 --> 历史分析` 中被用到.
"""

import configparser as cfgpsr
import os.path
import tkinter as tk
from tkinter.messagebox import showinfo


FILE_NAME = os.path.dirname(os.path.abspath(__file__)).rstrip('/') + '/config.ini'


headstr = '''
# PynAndPi - config.ini
#
#   - size: integer (7 to 12), default 9
#         The size of game window. (Default 803x688)
#         If it is set to 7, it'll be about 590x475;
#         If it is set to 12, it'll be about 1020x904.
#         In fact, it is the size of the canvas you throw the needles on.
#
#   - theme: light | dark
#         Set the color. 'light' for a bright color scheme,
#         and 'dark' for cool one.
#
#   - language: zh-hans | english
#       ! It's not implemented and I'm not going to.
#       ! The language is always Chinese,
#       ! - though this file is written in English!
#
#   - using_numpy: yes | no
#         Use Python third-party package `numpy` in throwing algorithm.
#
#   - using_matplotlib: yes| no
#         Use Python third-party package `matplotlib`.
#         It is used in `历史记录` -> `历史分析`.
#
'''.strip(
    '\n'
)

stdstr = '''
[Display]

size = {size}
theme = {theme}

[Language]

language = {language}

[Extension]

using_numpy = {using_numpy}
using_matplotlib = {using_matplotlib}
'''

CONF_NUM = 5

keys = [
    ('Display', 'size'),
    ('Display', 'theme'),
    ('Language', 'language'),  # !! not in plan !!
    ('Extension', 'using_numpy'),
    ('Extension', 'using_matplotlib'),
]

defaults = {
    'size': '9',
    'theme': 'light',
    'language': 'zh-hans',
    'using_numpy': 'yes',
    'using_matplotlib': 'no',
}

choices = [
    ('size', tuple(map(str, range(7, 13)))),
    ('theme', ('light', 'dark')),
    ('language', ('zh-hans',)),
    ('using_numpy', ('yes', 'no')),
    ('using_matpotlib', ('yes', 'no')),
]


class Reader:
    """读取、修改设置, 这将反映到主程序中."""

    __slots__ = ['Ls', 'Os', 'Vs', 'curcfg', 'fr', 'parser', 'win']

    def __init__(self):
        """读取当前设置."""
        self.curcfg = defaults.copy()

        self.parser = cfgpsr.ConfigParser()
        self.parser.read(FILE_NAME)
        for i in range(CONF_NUM):
            v = self.get(*keys[i])
            name = keys[i][1]
            self.curcfg[name] = v if v in choices[i][1] else defaults[name]

    @staticmethod
    def writeback(d=defaults):
        """
        将当前设置写回.

        .. note::
           这是一个 `static method`.

        Parameters
        ----------
        d: dict = defaults
            写回的字典. 默认值 ``defaults`` 字典是重置时使用的.
        """
        with open(FILE_NAME, 'w') as f:
            f.write(headstr)
            f.write('\n')
            f.write(stdstr.format(**d))

    def get(self, seg, name):
        """
        获取 `seg` 块 `name` 键的值.

        Parameters
        ----------
        seg: str
            字段名

        name: str
            键名

        Returns
        -------
        若 :menuselection:`seg --> name` 键存在则返回,
        否则, 返回 `defaults[name]`.
        """
        if self.parser.has_option(seg, name):
            return self.parser.get(seg, name, fallback=defaults[name])
        return defaults[name]

    def set(self, name, value):
        """将 `name` 键的值设为 `value`."""
        self.curcfg[name] = value

    def commit(self):
        """
        保存当前设置.

        .. note::
           显示 MessageBox :guilabel:`information`: 修改成功提示.
        """
        for i, v in enumerate(self.Vs):
            self.curcfg[keys[i][1]] = v.get()
        self.writeback(self.curcfg)
        showinfo('修改成功', '修改成功！将在下次运行时生效。')

    def reset(self):
        """
        重置当前设置.

        .. note::
           显示 MessageBox :guilabel:`information`: 重置成功提示.
        """
        self.curcfg = defaults.copy()
        self._update_optmenu()
        self.writeback()
        showinfo('重置成功', '重置成功！将在下次运行时生效。')

    def _update_optmenu(self):
        for i, v in enumerate(self.Vs):
            v.set(self.curcfg[keys[i][1]])

    def _start(self):
        win = tk.Tk()
        win.title('布丰投针 - 配置')
        fr1 = tk.Frame(win, bg='#fff')
        fr2 = tk.Frame(win, bg='#fff')

        Ls = [tk.Label(fr1, text=keys[i][1] + ' ', bg='#fff') for i in range(CONF_NUM)]
        Vs = [tk.StringVar() for _ in range(CONF_NUM)]
        Os = [tk.OptionMenu(fr1, Vs[i], *choices[i][1]) for i in range(CONF_NUM)]

        for i in range(CONF_NUM):
            Vs[i].set(self.curcfg[keys[i][1]])

        # place
        # labels for padding
        tk.Label(fr1, text=' ', bg='#fff').grid(row=0, column=0)
        tk.Label(fr1, text='  ', bg='#fff').grid(row=2, column=7)
        tk.Label(fr1, text='  ', bg='#fff').grid(row=4, column=7)
        for i in range(CONF_NUM):
            Ls[i].grid(row=i // 2 * 2 + 1, column=i % 2 * 3 + 1, sticky='e')
            Os[i].grid(row=i // 2 * 2 + 1, column=i % 2 * 3 + 2, sticky='ew')

        resetb = tk.Button(fr2, text=' 重置所有 ', command=self.reset)
        commitb = tk.Button(fr2, text='  确    定  ', command=self.commit)

        tk.Label(fr2, bg='#fff').grid(row=0, column=0)
        tk.Label(fr2, bg='#fff').grid(row=2, column=4)
        resetb.grid(row=1, column=1)
        commitb.grid(row=1, column=3)
        fr2colweight = [1, 1, 2, 1, 1]
        for i in range(5):
            fr2.grid_columnconfigure(i, weight=fr2colweight[i])
        for i in range(3):
            fr2.grid_rowconfigure(i, weight=1)

        fr1.pack(fill='x')
        fr2.pack(fill='x')

        self.win = win
        self.fr = fr1
        self.Ls = Ls
        self.Vs = Vs
        self.Os = Os

    def start(self):
        self._start()
        self.win.mainloop()


reader = None


def main():
    """" **设置** " 主程序."""
    global reader
    reader = Reader()
    reader.start()


if __name__ == '__main__':
    main()
