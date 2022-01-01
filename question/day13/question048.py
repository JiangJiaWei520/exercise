"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md
问题48
问题
定义一个名为Rectangle的类，它可以由长度和宽度来构造。矩形类有一个可以计算面积的方法。

提示
使用def methodName(self)定义一个方法。
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width


if __name__ == '__main__':
    area = Rectangle(2, 2).calc_area()
    print(area)
