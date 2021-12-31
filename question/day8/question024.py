"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md
问题 24
问题：
Python 有很多内置函数，如果你不知道如何使用它，你可以在线阅读文档或找一些书籍。但是 Python 对每个内置函数都有一个内置的文档函数。

请编写一个程序打印一些Python内置函数文档，如abs()、int()、raw_input()

并为您自己的功能添加文档

提示：
内置的文档方法是__doc__
"""
class Question024:
    def __init__(self):
        pass

    def testfun(self):
        """
            test
        """
        return 0

if __name__ == '__main__':
    help(abs)
    print("#############################################")
    help(int)
    print("############################################")
    print(help(Question024().testfun))
