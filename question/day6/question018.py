"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%206.md
问题18.
问题：
网站要求用户输入用户名和密码以注册。编写程序以检查用户输入的密码的有效性。
以下是检查密码的标准：
[a-z]之间至少1个字母
[0-9]之间的至少1个数字
[A-Z]之间至少1个字母
[$＃@]的至少1个字符
最小交易密码长度：6
最大交易密码长度：12
您的程序应接受一系列逗号分隔的密码，并根据上述标准检查它们。匹配标准的密码将被打印，每个密码由逗号分隔。

例子
如果以下密码作为对程序的输入给出：
ABd1234@1,a F1#,2w3E*,2We3345
然后，程序的输出应该是：
ABd1234@1
提示：
在提供输入数据的情况下，应该假设是控制台输入。
"""


class Question018:
    def __init__(self):
        pass

    def test_fun(self):
        # 提示输入密码
        i = input("请输入你要检查的密码，多个密码由由逗号分隔：").split(",")
        # print(i)
        for x in i:
            # 判断密码长度是否大于等于6，小于等于12
            # print(x)
            if 6 <= len(x) <= 12:
                isupperzimu = 0
                islowerzimu = 0
                shuzi = 0
                zifu = 0
                for y in range(len(x)):
                    # print(x[y] == '#')
                    if x[y].isdigit():  # 判断是数字的字符个数
                        shuzi += 1
                    elif x[y].isupper():  # 判断是大写字符的字符个数
                        isupperzimu += 1
                    elif x[y].islower():  # 判断是小写字符的字符个数
                        islowerzimu += 1
                    elif x[y] == '$' or x[y] == '#' or x[y] == '@':  # 判断包含$＃@字符的字符个数
                        # print(111)
                        zifu += 1
                    else:
                        pass
                # print(shuzi, isupperzimu, islowerzimu, zifu)
                if zifu >= 1 and shuzi >= 1 and islowerzimu >= 1 and isupperzimu >= 1:
                    print("匹配标准的密码有:", x)


if __name__ == "__main__":
    Question018().test_fun()
