"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
问题42
问题:
编写一个程序，map()和filter()可以生成一个元素为[1,2,3,4,5,6,7,8,9,10]偶数平方的列表。

提示:
使用map()生成列表。使用filter()过滤列表中的元素。使用lambda定义匿名函数。

filter()
    filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

    该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
    filter(function, iterable)
        参数
        function -- 判断函数。
        iterable -- 可迭代对象。
        返回值
        返回列表。
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listnum = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst))  # 将可迭代对象列表值循环放入匿名函数中进行计算返回一个新的可迭代列表对象
print(list(listnum))
