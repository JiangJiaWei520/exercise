"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_10.md
问题34
问题:
定义一个函数，它可以生成一个列表，其中的值是1到20之间的数的平方(两者都包含在内)。然后，函数需要输出列表中的前5个元素。

提示:
使用**运算符得到一个数字的幂。在循环中使用range()。使用list.append()向列表中添加值。使用[n1:n2]切片一个列表
"""


class Question034:
    def test_fun(self):
        lst = list()
        for x in range(1, 21):
            lst.append(x ** 2)

        print(lst[0:5])


if __name__ == '__main__':
    Question034().test_fun()