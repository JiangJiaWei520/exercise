"""
    来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
    问题：编编写一个程序，可以计算给定数字的阶乘。结果应该以逗号分隔的序列打印在一行上。假设向程序提供以下输入：8 那么，输出应该是：40320
    提示：如果向问题提供输入数据，则应假定它是控制台输入。
"""
class Question002:
    def __init__(self):
        pass

    def function(self):
        try:
            x = int(input("请输入需计算阶乘的数字：\n"))
            # 结果
            fact = 1
            while x >= 1:
                fact = fact * x
                x = x - 1
                # print(x)
            print("输入数字阶乘结果为:" + str(fact))
        except:
            print("输入不符合要求，请输入需计算阶乘的数字!")

# 程序入口
if __name__=='__main__':
    Question002().function();