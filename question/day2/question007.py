"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
问题 7
问题：
_编写一个程序，以 2 位数字 X，Y 作为输入并生成一个二维数组。数组第i行第j列的元素值应为i*j
注：i=0,1.., X-1；j=0,1,¡Y-1。假设程序有以下输入： 3,5
然后，程序的输出应该是：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
提示：
注意：如果向问题提供输入数据，则应假定它是逗号分隔形式的控制台输入。
"""


class Question007:
    def __init__(self):
        pass

    def test_fun(self):
        i = input("请输入以逗号分隔形式的二个数字：")
        value = list(i.split(","))
        # 定义一个X行，Y的列表
        result = [[0 for col in range(int(value[1]))] for row in range(int(value[0]))]
        # 循环获取值，存入到对应的列表中
        for x in range(0, int(value[0])):
            for y in range(0, int(value[1])):
                # print(x * y)
                result[x][y] = x*y
                # print("result[x][y]："+str(result[x][y]))
        print(result)


if __name__ == '__main__':
    Question007().test_fun()
