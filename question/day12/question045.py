"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_12.md
问题45
问题:
定义一个名为American的类，它有一个名为printNationality的静态方法。

提示:
使用@staticmethod装饰器来定义类的静态方法。另外还有两种方法。想了解更多，请访问这个链接。
"""


class American:
    @staticmethod
    def printNationality(num):
        return num


if __name__ == '__main__':
    american = American().printNationality(1)
    print(american)
