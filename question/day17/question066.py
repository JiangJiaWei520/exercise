"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

问题 66
问题
请编写一个从控制台接受基本数学表达式的程序并打印评估结果。

示例：如果给定以下 n 作为程序的输入：

35 + 3
那么，程序的输出应该是：

38
提示
使用 eval() 评估表达式。
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
eval( '3 * x' )
21
"""
i = input("输入基本数学表达式：")
result = eval(i)
print(result)
