"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md
问题57
问题
编写一个程序来读取一个ASCII字符串并将其转换为一个用utf-8编码的unicode字符串。

提示
使用unicode()/encode()函数进行转换。
"""
strtemp = input("输入字符串：")
lst = strtemp.encode('utf-8')
print(lst)