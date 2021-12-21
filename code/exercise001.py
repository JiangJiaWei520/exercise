"""
    来源：https://www.runoob.com/python/python-exercise-example1.html
    备注：pythonn练习实例1
    题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""


class Exercise01:
    for x in range(1, 5):
        for y in range(1, 5):
            for z in range(1, 5):
                if (x != y) and (x != z) and (y != z):
                    print(x, y, z)
