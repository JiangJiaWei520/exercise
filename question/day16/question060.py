"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md
问题60
问题
写一个程序来计算:
f(n)=f(n-1)+100 when n>0
and f(0)=0
给定n个输入(n>0)。

例如:如果下面的n作为程序的输入:
5

那么，程序的输出应该是:
500
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
我们可以在Python中定义递归函数。
"""


class Question060:
    def recursion(self, num):
        if num == 0:
            return 0
        else:
            return self.recursion(num - 1) + 100


if __name__ == '__main__':
    recursion = Question060().recursion(5)
    print(recursion)