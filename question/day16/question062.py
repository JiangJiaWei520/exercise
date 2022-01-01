"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md
问题62
问题
斐波那契数列的计算公式如下:
f (n)如果n = 0 = 0
f (n) = 1如果n = 1
f (n) = f (n - 1) + f (n - 2)如果n > 1
请写一个程序来计算f(n)的值与给定的n输入控制台。

例如:如果下面的n作为程序的输入:
7

那么，程序的输出应该是:
0, 1, 1, 2, 3, 5, 8, 13
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
我们可以在Python中定义递归函数。使用列表推导式从现有列表生成列表。使用string.join()来连接字符串列表。
"""


class Question062:
    def recursion(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        sequence = [0, 1]
        a, b = 0, 1
        for x in range(2, n + 1):
            c = a + b
            sequence.append(c)
            a = b
            b = c
        return sequence


if __name__ == '__main__':
    recursion = Question062().recursion(7)
    print(recursion)
