"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_14.md
问题53
问题
假设我们有一些“username@companyname.com”格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名，用户名和公司名都是由字母组成的。

示例:如果下列电子邮件地址被输入到程序:

john@google.com
那么，程序的输出应该是:

john
在向问题提供输入数据的情况下，应该假定它是一个控制台输入。

提示
使用\w匹配字母。
"""


class MatchAlph:
    """
        获取电子邮箱前缀
    """
    def match_alph(self, alph='xxx@xxx.xx'):
        # alph = 'john@google.com'
        lst=alph.split("@")
        print(lst[0])


if __name__ == '__main__':
    email = input("输入电子邮箱：")
    MatchAlph().match_alph(email)
