# &nbsp; &nbsp; ����Ͷ�룺Python GUI ���ģ��

<div style="text-align: center;">

![PynAndPi Icon](f_icon.png 'PynAndPi Icon')

</div>

>
> > ���ߣ�����
> > 
> > �汾�ţ�v1.1.0a
> > 
> > tips: ����������꣡
>

## &nbsp; &nbsp; 0x00���ļ��ṹ


&nbsp; &nbsp; *����Ϊ�ļ��ṹ����*


```
   PynAndPi/
       �����ļ��У�pyn �� pin ���ƣ���Ϊ�룬���� py ���� Python��pi �� �У�Բ���ʡ�
       |
       |- ʹ��˵��.html  - �ĵ��������ļ���
       |- ԭ�����.html  - �ĵ���֤�����㷨
       |- icon.png       - ͼƬ������ͼ��
       |
       |- main.pyw       - �������
       |
       +- photos/        - ͼƬ��PNG��ICON���ҵ�ͼ�ꡣ
       +- pinandpi/
           һ�� Python ����package����
           ���Ե����ŵ� PYTHON/Lib/site-packages �У�
           �� 'import pinandpi; pinandpi.main()' ���С�
           |
           |- __init__.py    - Python ���ĸ���
           |
           +- imagine/       - �㷨��
           |
           +- src/                
               Դ���ļ���
               |- __init__.py    - Python ���ĸ���
               |
               |- history.csv    - �� src �ڳ����������ʷ��¼�ļ���
               |- config.ini     - �����ļ���INI ��ʽ
               |
               |- ʹ��˵��.html  - �ĵ���Ҳ�����ļ�
               |- ԭ�����.html  - �ĵ���֤�����㷨
               |
               |- config.py      - ���ó���
               |- run.py         - �������ļ�
               |
               +- photos/        - ͼƬ��PNG��ICON���ҵ�ͼ�ꡣ
```



## &nbsp; &nbsp; 0x01���򿪷�ʽ

- ��� `main.pyw` ���С�

> New in 1.0.1:
> >�˰汾����ֱ�����У�Ҳ����Ϊ **`Python`** ģ�飨����ʹ�ã�
> >��Ϊģ��ʱ�뽫 `pinandpy �ļ���` ����``PYTHON/Lib/site-packages �ļ���``�С�
> >������һ������ GUI ����Ҳ����Ҫ�� import �Ǻ�  :-)��
> >
> >�������Ϊģ�飨������������ [**`PyPI`**](https://pypi.org) �Ͼ��ǿ�ϧ�ˣ������Ҳ��ᡭ�� ��

## &nbsp; &nbsp; 0x02�������ص�

<br />

&nbsp;&nbsp; ʹ�� [**`Python(CPython)`**](https://www.python.org) ��д��û�������д��ڣ�
ֻ��ʹ�� [**`tkinter`**](https://docs.python.org/zh-cn/3/library/tkinter.html) ���Ƶ� `GUI` ���档

ע��

- ��ʹ��`.pyw`�ļ�**˫������**����û�������д��ڣ�
- ������չ����Ϊ `.py`������������д��ڣ�
- �� **`IDLE Edit Window`** �����У����� IDLE �������档

&nbsp; &nbsp; ��������**����**��ϣ�����ϲ�� :D


## &nbsp;&nbsp; 0x03�������淨��

```Python
   pass    # Python �ؼ��֣�ʲôҲ������ռλ�á�
```
������Ц������ ;)

1. ��� **`��ʼͶ��`**��
2. ��`������`ѡ��ģʽ��
    - ����ģʽ��һֱͶ�룬������������ÿ 500,0000 ����ˢ��һ�Φ�ֵ��
    - �ǳ���ģʽ����ѡ��ÿ��Ͷ��������Ҳ�л���/����������֡�
    - ��ť��Ϊ����ɫ��Ϊ��������ɫΪ�رա�

    �� **`���¿�ʼ`** �����㵱ǰ���ȡ�
3. 
    + ��`������`�п�ʼ��ť��ѡ��Ͷ�����İ�ť��Ͷ���ڼ俪ʼ��ť����ֹͣ����������ť�����á�

    + **`��ʷ��¼`**�У�����ѡȡ��ʷ��¼��Ҳ���Ա�����ȣ��������� **`matplotlib`** �ļ�¼������
    [**`matplotlib`**](https://matplotlib.org 'matplotlib����')
    �� Python �ĵ�������������ѧ�йص����벻�� [`numpy`](https://numpy.org 'numpy����'), `matplotlib`,
        [`pandas`](https://pandas.pydata.org)��,
    ��Ҫ���ذ�װ��
    ���������У�
        ```
        .> python3 -m pip install --upgrade numpy
        .> python3 -m pip install --upgrade matplotlib
        ```
        Ȼ�󣬵ȴ�������ɣ��� **Python** �У�
        ```Python
        import matplotlib
        ```
        û�б�����У� :-)

## &nbsp;&nbsp; 0x04��ע������

&nbsp;&nbsp; ������Ҫ�Ķ��κ��ļ������Ըı���� `config.ini`���������ļ���

> New in 1.1.0:
> > ���ڣ�����û�д����������쳣������ `config.py` ����д����ȷ���ݡ�
> >

## &nbsp; &nbsp; 0x05��֤�����㷨

&nbsp;&nbsp; �� [*�ĵ���֤�����㷨*](int.html),
�������Ҫ������һ����΢���֡������ۻ�����������ô��ľͲ�Ҫ����
    :stuck_out_tongue_winking_eye:��

<br />

<div style="background:#ddd">

<br />

<small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
���ĵ�ʹ�� **`Visual Studio 2022`**
�е� `Markdown` ���д�ɲ�תΪ `html` �ļ���
</small>

<br />

</div>
