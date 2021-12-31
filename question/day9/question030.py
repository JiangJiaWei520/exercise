"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md
第 30 题
问题：
定义一个可以接受两个字符串作为输入的函数，并在控制台中打印最大长度的字符串。如果两个字符串的长度相同，则该函数应逐行打印所有字符串。

提示：
使用 len() 函数获取字符串的长度。
"""
class Question030:
    def test_fun(self,str1,str2):
        if len(str1)>=len(str2):
            print(str1)
        elif len(str1)<len(str2):
            print(str2)
        else:
            print('不合法输入')

if __name__ == '__main__':
    Question030().test_fun('ads','sadsdsad')