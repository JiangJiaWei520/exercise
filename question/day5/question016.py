"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%205.md
问题 16
问题：
使用列表推导式对列表中的每个奇数进行平方。该列表由逗号分隔的数字序列输入。>假设向程序提供以下输入：
1,2,3,4,5,6,7,8,9
然后，输出应该是：
1,9,25,49,81
提示：
如果向问题提供输入数据，则应假定它是控制台输入。
"""
class Question016:
    def __init__(self):
        pass

    def test_fun(self):
        l = list(input("输入由逗号分隔的数字序列:").split(","))
        #print(l,range(len(l)),l[0])
        # 遍历判断每个值是否为奇数，返回奇数的值并进行平方
        # result = [ int(l[x])**2 for x in range(len(l)) if (int(l[x])%2) !=0 ]
        result = [int(x) ** 2 for x in l if (int(x) % 2) != 0]
        print(result)

if __name__ == "__main__":
    Question016().test_fun()