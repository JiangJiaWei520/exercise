"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md
问题49
问题
定义一个名为Shape的类及其子类Square。Square类有一个init函数，参数为length。这两个类都有一个area函数，它可以打印shape的区域，其中shape的区域默认为0。

提示
要重写超类中的方法，可以在超类中定义具有相同名称的方法。
"""


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        self.length = length

    def area(self):
        return self.length * 2


if __name__ == '__main__':
    area = Square(2).area()
    print(area)
