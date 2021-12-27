"""
来源：
问题 15
问题：
编写一个程序，用给定的数字作为 a 的值计算 a+aa+aaa+aaaa 的值。
假设向程序提供以下输入：
9
然后，输出应该是：
11106
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
解析：
计算 a+aa+aaa+aaaa 的和
"""
class Question015:
    def __init__(self):
        pass

    def test_fun(self):
        i = input("请输入一个数字：")
        result = 0
        for x in range(1,5):
            result += int(i*x)
        print("a+aa+aaa+aaaa 的和为：",result)


if __name__ == "__main__":
    Question015().test_fun()
