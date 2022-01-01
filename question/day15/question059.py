"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md
问题59
问题
写一个程序来计算1/2+2/3+3/4+…+n/n+1与给定的n输入控制台(n>0)。

例如:如果下面的n作为程序的输入:

5
那么，程序的输出应该是:

3.55
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
使用float()将整数转换为浮点数。即使没有转换，也不会引起问题，因为python默认情况下理解值的数据类型
"""
i = int(input("输入数据："))
val = 0.0
for x in range(1,i+1):
    val += x/(x+1)
print(val)