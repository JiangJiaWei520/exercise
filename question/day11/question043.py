"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
问题43
问题:
编写一个程序，它可以filter()生成一个元素为1到20之间的偶数的列表(都包含在内)。

提示:
使用filter()过滤列表中的元素。使用lambda定义匿名函数。
"""
lst = list()
for x in range(1,21):
    lst.append(x)
listnum = map(lambda x: x, filter(lambda x: x % 2 == 0, lst))  # 将可迭代对象列表值循环放入匿名函数中进行计算返回一个新的可迭代列表对象
print(list(listnum))
