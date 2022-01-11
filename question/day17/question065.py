"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

问题
请编写断言语句来验证列表 [2,4,6,8] 中的每个数字是否为偶数。
提示
使用“断言表达式”进行断言。
关键字assert
语法格式如下：
assert expression
等价于：

if not expression:
    raise AssertionError
"""
# lst = [2, 4, 6, 8, 9]
lst = [2, 4, 6, 8]
for x in lst:
    assert x % 2 == 0
