"""
来源 ：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
问题 9
问题：
编写一个程序，接受行序列作为输入，并在使句子中的所有字符大写后打印行。

假设向程序提供以下输入：

Hello world
Practice makes perfect
然后，输出应该是：

HELLO WORLD
PRACTICE MAKES PERFECT
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
"""


class Question009:
    def __init__(self):
        pass

    def test_fun(self):
        result = input("请输入以逗号分隔形式的字符：").upper()
        print(result)


if __name__ == "__main__":
    Question009().test_fun()
