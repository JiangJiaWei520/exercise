"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_12.md
问题44
问题:
编写一个程序，它可以映射()生成一个元素为1到20之间数的平方的列表(两者都包含在内)。

提示:
使用map()生成列表。使用lambda定义匿名函数。
"""
lst = list()
listnum = map(lambda x: x ** 2, range(1, 21))
print(list(listnum))