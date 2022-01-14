"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md
问题72
问题
请编写一个程序来生成一个包含100和200之间的5个随机数的列表。

提示
使用random.sample()生成一个随机值列表。
"""
import random

temp = [i for i in range(100, 201)]
result = random.sample(temp, 5)
print(result)
