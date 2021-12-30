"""
来源：
问题 20
问题：
定义一个带有生成器的类，该生成器可以在给定范围 0 和 n 之间迭代可被 7 整除的数字。
假设向程序提供以下输入：
7
然后，输出应该是：
0
7
14
提示：
考虑使用类、函数和理解。
"""
class Question:
    def __init__(self):
        pass

    """
        测试方法
    """
    def test_fun(self):
        """
            迭代可被 7 整除的数字的方法
        """
        # 接收控制台输入的数字
        i = int(input("请输入一个用于迭代的数字："))
        # 定义一个接收结果的列表
        result = list()
        # 循环遍历，找出可以被7整除的数字
        for x in range(1,i):
            if x%7 == 0 :
                result.append(x)
            else:
                pass
        # 输出打印结果
        print(result)


if  __name__ == '__main__':
    Question().test_fun()