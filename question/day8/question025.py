"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md
问题 25
问题：
定义一个类，它有一个类参数并且有一个相同的实例参数。

提示：
定义一个实例参数，需要在__init__方法中添加。可以用construct参数初始化一个对象，也可以稍后设置值
"""
class Question025:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age

if __name__ == '__main__':
    que=Question025('张三','18')
    print(que.name,que.age)

    que2=Question025()
    que2.name='李四'
    que2.age=22
    print(que2.name,que2.age)