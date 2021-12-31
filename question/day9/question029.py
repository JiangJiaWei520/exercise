"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md
问题 29
问题：
定义一个函数，可以接受两个字符串作为输入并将它们连接起来，然后在控制台中打印出来。

提示：
使用 + 号连接字符串。
"""
class Question029:
    def test_fun(self,str1,str2):
        print(str1+str2)

if __name__ == '__main__':
    Question029().test_fun('张三','你好!')