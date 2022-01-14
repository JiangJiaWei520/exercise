"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md
问题71
问题
请编写一个程序输出一个随机数，可以被5和7整除，10和150之间使用随机模块和列表推导。

提示
对列表中的随机元素使用random.choice()
"""
import random

temp = [i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]
result = random.choice(temp)
print(result)
