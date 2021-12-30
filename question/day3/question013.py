"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md
问题 13
问题：
编写一个程序，接受一个句子并计算字母和数字的个数。
假设向程序提供以下输入：
hello world! 123
然后，输出应该是：
LETTERS 10
DIGITS 3

提示：
如果向问题提供输入数据，则应假定它是控制台输入。
isnumeric() 是否数字
isalpha() 是否字母
"""
class Question013:
    def __init__(self):
        pass

    def test_fun(self):
        # 接受一个句子并计算字母和数字的个数。
        juzi = input("请输入一个句子：")
        # 累加计算字母和数字个数
        dic = d = {"DIGITS":0, "LETTERS":0}
        #print(juzi,juzi[0])
        # 循环判断字符
        for x in range(len(juzi)):
            #print(juzi.isalpha(),juzi.isdigit())
            # 判断是否是字母
            if juzi[x].isalpha():
                d["LETTERS"] += 1
                #print(i)
            #  判断是否是数字
            elif juzi[x].isdigit():
                d["DIGITS"] += 1
            #  非数字或者字母无条件通过
            else:
                pass

        print(d)

if __name__ == "__main__":
    Question013().test_fun()