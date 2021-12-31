"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_10.md
第 32 题
问题：
定义一个函数，它可以生成一个字典，其中键是 1 到 20 之间的数字（都包括在内），值是键的平方。该函数应该只打印键。

提示：
使用dict[key]=value模式将条目放入字典。使用**运算符得到一个数字的幂。在循环中使用range()。使用keys()迭代字典中的键。我们也可以使用item()来获取键/值对。
"""
class Question032:
    def dictionary(self):
        dictionary=dict()
        for x in range(1,21):
            dictionary[x]=x**2

        # print(dictionary.keys())
        # print(dictionary.items())
        for key,value in dictionary.items():
            print(key, value)
        # for x in dictionary:
            # print(x)

if __name__ =='__main__':
    Question032().dictionary()