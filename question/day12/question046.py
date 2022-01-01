"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_12.md
问题46
问题:
定义一个名为American的类及其子类NewYorker。

提示:
使用class Subclass(ParentClass)定义一个子类
"""


class American:
    @staticmethod
    def printNationality(num):
        return num


class NewYorker(American):
    def __init__(self):
        pass

    @staticmethod
    def printNationality(num):
        return num**2


if __name__ == '__main__':
    # american = American().printNationality(2)
    # print(american)
    newyorker = NewYorker().printNationality(2)
    print(newyorker)
