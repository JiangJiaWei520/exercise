"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md
问题 22
问题：
编写一个程序来计算输入中单词的频率。输出应在按字母数字顺序对键进行排序后输出。
假设向程序提供以下输入：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
然后，输出应该是：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
提示
如果向问题提供输入数据，则应假定它是控制台输入。
分析：
1、统计单词频率，假定以空格划分单词
2、排序
"""
class Question022:
    def __init__(self):
        pass

    def calculate(self):
        # 接收输入，以空格分隔
        i = input("输入需要计算的单词串，以空格分隔：").split(" ")
        i.sort()
        dict_value =dict()
        for x in i:
            dict_value[x]=i.count(x)

        for x in dict_value:
            print(x+":"+str(dict_value[x]))

        # print(i)



if __name__ == '__main__':
    Question022().calculate()