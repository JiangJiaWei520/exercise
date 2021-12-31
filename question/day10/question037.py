"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_10.md
问题37
问题:
定义一个函数，它可以生成和打印一个元组，其中值是1到20之间数的平方(两者都包括在内)。

提示:
使用**运算符得到一个数字的幂。在循环中使用range()。使用list.append()向列表中添加值。使用tuple()从列表中获取一个元组。
"""


class Question037:
    def test_fun(self):
        lst = list()
        for x in range(1, 21):
            lst.append(x ** 2)

        print(tuple(lst))


if __name__ == '__main__':
    Question037().test_fun()