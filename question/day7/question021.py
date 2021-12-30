"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%207.md
问题 21
问题：
机器人在从原点 (0,0) 开始的平面中移动。机器人可以按照给定的步数向上、向下、向左和向右移动。机器人运动轨迹如下图所示：
UP 5
DOWN 3
LEFT 3
RIGHT 2
方向后面的数字是步数。请编写一个程序来计算经过一系列运动和原点后到当前位置的距离。如果距离是浮点数，则只打印最接近的整数。 示例： 如果将以下元组作为程序的输入给出：
UP 5
DOWN 3
LEFT 3
RIGHT 2
然后，程序的输出应该是：
2
提示：
如果向问题提供输入数据，则应假定为控制台输入。此处距离表示欧氏距离。导入数学模块以使用 sqrt 函数。
解析：
计算直线距离

"""
# 导入数学模块sqrt
from math import sqrt


class Question021:
    def __init__(self):
        pass

    def test_fun(self):
        up = 0
        down = 0
        left = 0
        right = 0
        while True:
            # 定义变量接收移动距离，假定以空格为分割
            i = input("请输入移动距离，假定以空格为分割，回车结束移动：").split(" ")
            if not i[0]:
                break
            elif 'UP' in i:
                up += int(i[1])
            elif 'DOWN' in i:
                down += int(i[1])
            elif 'LEFT' in i:
                left += int(i[1])
            elif 'RIGHT' in i:
                right +=int(i[1])
            else:
                pass
        # 求值
        print('移动结束，始点和终点的距离是：',round(sqrt((up-down)*2+(left-right)*2)),(up-down),(left-right))


if __name__ == '__main__':
    Question021().test_fun()
