"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md
问题 27
问题：
定义一个可以将整数转换为字符串并在控制台中打印的函数。
提示：
使用 str() 将数字转换为字符串。
"""
class Question027:
    def test_fun(self,num):
        return str(num)

if __name__ == '__main__':
    que=Question027().test_fun(23.2)
    print(que,type(que))