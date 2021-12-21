"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
问题 6
问题：
编写一个程序，根据给定的公式计算并打印值：
Q = [(2*C*D)/H]的平方根
以下是 C 和 H 的固定值：
C 是 50。H 是 30。
D 是变量，其值应该以逗号分隔的序列输入到您的程序中。例如，让我们假设以下逗号分隔的输入序列被提供给程序：
100,150,180
程序的输出应该是：
18,22,24

18 = [(2 *50 *100)/30] 的平方根
提示：
如果接收到的输出是十进制形式，则应将其四舍五入到最接近的值（例如，如果接收到的输出是 26.0，则应打印为 26）。如果向问题提供输入数据，则应假定为控制台输入。
"""
import math


class Question006:

    def __init__(self):
        pass

    def test(self):
        C = 50
        H = 30
        x = input("请以逗号分隔的数字输入到您的程序中：")
        mylist = x.split(",")
        Q = list()
        # print(mylist)
        for D in mylist:
            Q.append(round(math.sqrt((2 * C * int(D)) / H)))

        print(Q)


if __name__ == "__main__":
    Question006().test()
