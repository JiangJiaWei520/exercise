"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

问题68
问题
请使用Python模块生成一个随机浮点数，其值在10到100之间。

提示
使用random.random()在[0,1]中生成一个随机浮点数。
"""
import random


class Question068:
    def test(self):
        print(random.uniform(10, 100))


if __name__ == '__main__':
    Question068().test()