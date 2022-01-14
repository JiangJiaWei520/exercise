"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md
问题70
问题
请写一个程序输出一个随机的偶数0和10之间的使用随机模块和列表理解。

提示
对列表中的随机元素使用random.choice()。
"""
import random

temp = [i for i in range(0, 11)]
result = random.choice(temp)
print(result)