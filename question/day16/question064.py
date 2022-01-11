"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md
问题 64
问题
请使用生成器编写一个程序，以逗号分隔的形式打印 0 和 n 之间可以被 5 和 7 整除的数字，而 n 由控制台输入。

示例：如果给定以下 n 作为程序的输入：

100
那么，程序的输出应该是：

0,35,70
如果向问题提供输入数据，则应假定它是控制台输入。

提示
使用 yield 在生成器中生成下一个值。
"""
lst = list()
i = int(input("输入一个大于0的整数："))
for x in range(0,i+1):
    if x % 5 == 0 and x % 7 == 0:
        lst.append(x)
print(lst)