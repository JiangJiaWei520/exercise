"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%205.md
问题 17
问题：
编写一个程序，根据控制台输入的交易日志计算银行账户的净金额。事务日志格式如下所示：
D 100
W 200
D 表示存款，W 表示取款。
假设向程序提供以下输入：
D 300
D 300
W 200
D 100
然后，输出应该是：
500
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
提示：
strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
"""


class Question017:
    def __init__(self):
        pass

    def test_fun(self):
        # pass
        D = 0
        W = 0
        try:
            while True:
                i = input("请以换行符输入存款或者取款金额，或者直接回车结束存款、取款：")
                print(i)
                if not i:
                    break
                elif 'D' in i:
                    # print(i.strip("D "))
                    D += int(i.strip("D "))
                elif 'W' in i:
                    # print(i.strip("W "))
                    W += int(i.strip("W "))
                else:
                    pass
        except():
            print("输入格式有误，请按提示输入存款或者取款金额！")

        result = D - W
        print("存款或者取款结束，银行账户的净金额为：", result)


if __name__ == "__main__":
    Question017().test_fun()
