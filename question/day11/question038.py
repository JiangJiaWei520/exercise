"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
第 38 题
问题：
使用给定的元组 (1,2,3,4,5,6,7,8,9,10)，编写一个程序，在一行中打印前半个值，在一行中打印后半个值。

提示：
使用 [n1:n2] 表示法从元组中获取切片。
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tup), tup[0:int(len(tup)/2)])
