"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
第 41 题
问题：
编写一个程序，可以将 map() 生成一个列表，该列表的元素是 [1,2,3,4,5,6,7,8,9,10] 中元素的平方。

提示：
使用 map() 生成列表。使用 lambda 定义匿名函数。
map是python内置函数，会根据提供的函数对指定的序列做映射。

    map()函数的格式是：

    map(function,iterable,...)
    第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。

    把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。

# lambda匿名函数
    f = lambda a,b,c: a+b+c

    print f(1,2,3)
    结果为 6

    在代码：f = lambda a,b,c: a+b+c 中，lambda表示匿名函数，
    冒号 “：”之前的a,b,c表示它们是这个函数的参数。
    匿名函数不需要return来返回值，表达式本身结果就是返回值。
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listnum = map(lambda x: x ** 2,lst)  # 将可迭代对象列表值循环放入匿名函数中进行计算返回一个新的可迭代列表对象
print(list(listnum))
