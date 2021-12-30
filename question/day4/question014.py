"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%204.md
问题 14
问题：
编写一个程序，接受一个句子并计算大写字母和小写字母的个数。
假设向程序提供以下输入：
Hello world!
然后，输出应该是：
UPPER CASE 1
LOWER CASE 9
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
"""


class Question015:
    def __init__(self):
        pass

    def test_fun(self):
        i = input("请输入一个句子：")
        result = {"upper":0,"lower":0}
        for x in range(len(i)):
            if i[x].isupper():
                result["upper"] +=1
            elif i[x].islower():
                result["lower"] +=1
        print(result)

if __name__ == "__main__":
    Question015().test_fun()
