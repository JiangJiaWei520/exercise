"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md
问题 11
问题
编写一个程序，它接受一系列逗号分隔的 4 位二进制数作为输入，然后检查它们是否可以被 5 整除。可被 5 整除的数字将以逗号分隔的顺序打印。
例子：
0100,0011,1010,1001
那么输出应该是：
1010
注意：假设数据是通过控制台输入的。
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
二进制转十进制：
    例：将1110110转换为十进制数
    解：先将其转换为字符串，再使用int函数，指定进制转换为十进制。
    print(int("100111",2))
"""
class Question011:
    def __init__(self):
        pass

    def test_fun(self):
        str_num = input("请以逗号分隔的 4 位二进制数作为输入：").split(",")
        int_list = list()
        for x in range(len(str_num)):
            #print(str_num,str_num[x])
            int_num = int(str_num[x],2)
            print(int_num)
            if int_num%5 == 0:
                #print(str_num)
                int_list.append(str_num[x])

        print(int_list)
        # for x in range(len(int_list)):
        #     print(int_list[x],sep=",")

if __name__ == "__main__":
    Question011().test_fun()
