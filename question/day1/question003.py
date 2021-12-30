"""
    来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
问题：
使用给定的整数 n，编写一个程序来生成一个包含 (i, ixi) 的字典，该字典是 1 和 n 之间的整数（都包括在内）。然后程序应该打印字典。假设以下输入被提供给程序：8
然后，输出应该是：
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
提示：
如果向问题提供输入数据，则应假定为控制台输入。考虑使用 dict()
"""
class Question003:
    def __init__(self):
        pass


    def function(self):
        dict1=dict()
        n=int(input("请输入生成一个包含 (i, ixi) 字典的数字：\n"))
        for x in range(1,n+1):
            if x>=1 :
                dict1[x]=x**2
                #print(x,dict1)
                x=x-1
        print(dict1)

# 程序入口
if __name__=='__main__':
    Question003().function()