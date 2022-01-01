"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md
第 40 题
问题：
编写一个接受字符串作为输入的程序，如果字符串为“yes”或“YES”或“Yes”，则打印“Yes”，否则打印“No”。

提示：
使用 if 语句判断条件。
"""
i = input("输入字符串：")
if i == 'yes' or i == 'YES' or i == 'Yes':
    print('Yes')
else:
    print('No')
