"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md
问题61
问题
斐波那契数列的计算公式如下:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
请写一个程序来计算f(n)的值与给定的n输入控制台。

例如:如果下面的n作为程序的输入:
7
那么，程序的输出应该是:
13
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
我们可以在Python中定义递归函数。
"""


class Question061:
    def recursion(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return self.recursion(num - 1) + self.recursion(num - 2)


if __name__ == '__main__':
    recursion = Question061().recursion(7)
    print(recursion)
