"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_10.md
问题36
问题:
定义一个函数，它可以生成一个列表，其中的值是1到20之间的数的平方(两者都包含在内)。然后，该函数需要打印列表中除前5个元素外的所有值。

提示:使用**运算符获取数字的幂次。在循环中使用range()。使用list.append()向列表中添加值。使用[n1:n2]切片一个列表
"""


class Question036:
    def test_fun(self):
        lst = list()
        for x in range(1, 21):
            lst.append(x ** 2)

        print(lst[5:])


if __name__ == '__main__':
    Question036().test_fun()