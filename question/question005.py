"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
问题 5
问题：
定义一个至少有两个方法的类：

getString：从控制台输入获取字符串
printString：以大写形式打印字符串。
还请包括简单的测试函数来测试类方法。

提示：
使用init方法构造一些参数
"""


class Question005:

    def __init__(self):
        self.s = ""

    def get_string(self):
        """
        作用：getString：从控制台输入获取字符串
        """
        self.s = input("请输入你想输入的字符串：")

    def print_string(self):
        """
        作用：printString：以大写形式打印字符串。
        """
        print(self.s.upper())


if __name__ == '__main__':
    x = Question005()
    x.get_string()
    x.print_string()
    # 创建了二个对象，无法打印控制台输入值
    # Question005().get_string()
    # Question005().print_string()
