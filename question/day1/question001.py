"""
    来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
    问题：编写一个程序，找出 2000 到 3200（两者都包括在内）之间所有能被 7 整除但不是 5 的倍数的数字。得到的数字应以逗号分隔的顺序打印在一行上。
    提示：考虑使用 range(#begin, #end) 方法。
"""
class Question001:
    def __init__(self):
        pass

    def function(self):
        l=[]
        for x in range(2000,3201):
            if x%7==0 and x%5 !=0 :
                #print(x)
                l.append(x)
        print(l)

# 程序入口
if __name__=='__main__':
    Question001().function();