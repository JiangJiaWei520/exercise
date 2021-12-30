"""
    来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
问题 4
问题：
编写一个程序，它接受来自控制台的一系列以逗号分隔的数字，并生成一个列表和一个包含每个数字的元组。假设向程序提供以下输入：

34,67,55,33,12,98
然后，输出应该是：

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
提示：
如果向问题提供输入数据，则应假定为控制台 input.tuple() 方法可以将列表转换为元组
"""

class Question004:
    def __init__(self):
        pass

    def function(self):
        x = input("请输入一系列以逗号分隔的数字：")
        list= x.split(",")
        t=tuple(list)
        print(list,"\n",t)


# 程序入口
if __name__=='__main__':
    Question004().function()