"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md
第 54 题
问题
假设我们有一些“ username@companyname.com ”格式的电子邮件地址，请编写程序来打印给定电子邮件地址的公司名称。用户名和公司名都只由字母组成。

示例：如果将以下电子邮件地址作为程序的输入提供：

john@google.com
然后，程序的输出应该是：

google
如果向问题提供输入数据，则应假定它是控制台输入。

提示
使用 \w 匹配字母。


"""


class MatchAlph:
    """
        获取电子邮箱前缀
    """

    def match_alph(self, alph='xxx@xxx.xx'):
        # alph = 'john@google.com'
        lst = alph.split("@")
        lst1 = lst[1].split(".")
        print(lst1[0])


if __name__ == '__main__':
    email = input("输入电子邮箱：")
    MatchAlph().match_alph(email)
