"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
第 39 题
问题：
编写一个程序来生成并打印另一个元组，其值为给定元组 (1,2,3,4,5,6,7,8,9,10) 中的偶数。
提示：
使用“for”来迭代元组。使用 tuple() 从列表生成元组。
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst = list()
for x in tup:
    if int(x) % 2 == 0:
        lst.append(x)
        print(x)
    else:
        pass
print(lst, tuple(lst))
