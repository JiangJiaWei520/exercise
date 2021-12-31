"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md
问题 28
问题：
定义一个函数，它可以接收字符串形式的两个整数并计算它们的和，然后在控制台中打印出来。
提示：
使用 int() 将字符串转换为整数。
"""
class Question028:
    def test_fun(self,str1,str2):
        # print(str1,str2)
        return int(str1)+int(str2)

if __name__ == '__main__':
    que=Question028().test_fun('2','3')
    print(que)