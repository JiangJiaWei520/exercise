"""
来源：
第 31 题
问题：
定义一个函数，它可以打印一个字典，其中键是 1 到 20 之间的数字（都包括在内），值是键的平方。

提示：
使用 dict[key]=value 模式将条目放入字典中。使用 ** 运算符获取数字的幂。使用 range() 进行循环。
"""
class Question031:
    def dictionary(self):
        dictionary = dict()
        for x in range(1,21):
            dictionary[x] = x**2
        print(dictionary)


if __name__ == '__main__':
    Question031().dictionary()