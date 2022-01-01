"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_14.md
问题52
问题
定义一个以字符串消息作为属性的自定义异常类。

提示
要定义自定义异常，需要定义一个继承自exception的类。

raise语句
    为了引发异常，可以使用一个类（应该是Exception的子类）或者实例参数调用raise语句。
    raise语法格式如下：
    raise [Exception [, args [, traceback]]]
    语句中 Exception 是异常的类型（例如，NameError）参数标准异常中任一种，args 是自已提供的异常参数。
    最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。
"""


class CustomException(Exception):
    """
        以字符串消息作为属性的自定义异常类
    """

    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    try:
        num = int(input("输入值："))
        if num < 10:
            raise CustomException("值小于十")
        elif num >= 10:
            raise CustomException('值大于十')
    except CustomException as ce:
        print('异常信息为：' + ce.message)
