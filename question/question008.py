"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
问题 8
问题：
编写一个程序，接受逗号分隔的单词序列作为输入，并在按字母顺序排序后以逗号分隔的序列打印单词。

假设向程序提供以下输入：

without,hello,bag,world
然后，输出应该是：

bag,hello,without,world
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
"""


class Question008:
    def  __init__(self):
        pass

    def test_fun(self):
        result = input("请输入以逗号分隔形式的字符：").split(",")
        result.sort()
        print(result)


if __name__ == "__main__":
    Question008().test_fun()