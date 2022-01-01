"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md
第 55 题
问题
编写一个程序，它接受由空格分隔的一系列单词作为输入，以打印仅由数字组成的单词。

示例：如果将以下单词作为程序的输入给出：

2 cats and 3 dogs.
然后，程序的输出应该是：

['2', '3']
如果向问题提供输入数据，则应假定它是控制台输入。

提示
使用 re.findall() 使用正则表达式查找所有子字符串。
"""
import re


class Question055:
    str = '2 cats and 3 dogs.'
    print(re.findall('\d', str))  # [‘aab', ‘aab']
