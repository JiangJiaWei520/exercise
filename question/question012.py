"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md
问题 12
问题：
编写一个程序，找出 1000 到 3000（均包括在内）之间的所有数字，使得该数字的每一位都是偶数。得到的数字应以逗号分隔的顺序打印在一行上。

提示：
如果向问题提供输入数据，则应假定它是控制台输入。
"""
class Question012:
    def __init__(self):
        pass

    def test_fun(self):
        lst = list()
        # 循环获取1000到3000的值
        for x in range(1000,3001):
            # 循环判断值每一位数是否都是偶数
            for y in range(0,len(str(x))):
                # 判断每一位是否都是偶数（非0非奇数）
                if int(str(x)[y])%2 == 0 and int(str(x)[y])  != 0:
                    # 在最后一位都满足条件时，打印
                    if y == len(str(x))-1:
                        #print(x,y,str(x)[y],int(str(x)[y])%2,int(str(x)[y]),len(str(x))-1,sep=",")
                        print('结果',x,sep=",")
                        lst.append(x)
                else:
                    break
        print("最终结果为：",lst)

if __name__ == "__main__":
    Question012().test_fun()