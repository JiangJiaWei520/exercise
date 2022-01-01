"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md
问题47
问题
定义一个名为Circle的类，它可以由一个半径来构造。Circle类有一个可以计算面积的方法。

提示
使用def methodName(self)定义一个方法。
"""


class Circle:
    @staticmethod
    def circle_area(r):
        return 3.14*r**2


if __name__ == '__main__':
    circle_area = Circle().circle_area(2)
    print(circle_area)