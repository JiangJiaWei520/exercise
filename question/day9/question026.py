"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md
问题 26
问题：
定义一个可以计算两个数之和的函数。
提示：
定义一个带有两个数字作为参数的函数。您可以在函数中计算总和并返回值。
"""
class Question026:

    def test_fun(self,num1,num2):
        return num1+num2


if __name__ == '__main__':
    que=Question026().test_fun(2,3)
    print(que)