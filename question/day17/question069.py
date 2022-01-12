"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

问题69
问题
请使用Python模块生成一个随机浮点数，其值在5到95之间。

提示
使用random.random()在[0,1]中生成一个随机浮点数。
"""
import random


class Question068:
    def test(self):
        print(random.uniform(5, 95))


if __name__ == '__main__':
    Question068().test()