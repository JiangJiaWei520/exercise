"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md
问题73
问题
请编写一个程序，随机生成一个100和200(含)之间的5个偶数列表。

提示
使用random.sample()生成一个随机值列表
"""
import random

temp = [i for i in range(100, 201) if i % 2 == 0]
result = random.sample(temp, 5)
print(result)
