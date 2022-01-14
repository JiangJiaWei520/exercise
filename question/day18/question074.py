"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md
问题74
问题
请编写一个程序，随机生成一个包含5个数字的列表，可以被5和7整除，范围在1和1000之间。

提示
使用random.sample()生成一个随机值列表。
"""
import random

temp = [i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0]
print(temp)
result = random.sample(temp, 5)
print(result)
