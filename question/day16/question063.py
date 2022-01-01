"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md
问题63
问题
当n由控制台输入时，请编写一个程序，使用生成器以逗号分隔形式输出0到n之间的偶数。

例如:如果下面的n作为程序的输入:
10

那么，程序的输出应该是:
0、2、4、6、8、10
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
使用yield在generator中生成下一个值。
"""
lst = list()
i = int(input("请输入一个数值："))
for x in range(0, i+1):
    if x % 2 == 0:
        lst.append(x)
    else:
        pass

print(lst)
