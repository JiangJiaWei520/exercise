"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_14.md
问题51
问题
写一个函数来计算5/0，然后使用try/except来捕获异常。
提示
使用try/except来捕获异常。
"""


class ExceptCls:
    def calc(self):
        val = 0
        try:
            val = int(5 / 0)
            print(val)
        except ZeroDivisionError:
            print('除数不能为0')
        finally:
            pass


if __name__ == '__main__':
    ExceptCls().calc()
