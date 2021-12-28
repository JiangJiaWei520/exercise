"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%206.md
问题 19
问题：
您需要编写一个程序来按升序对 (name, age, score) 元组进行排序，其中 name 是字符串，age 和 score 是数字。元组由控制台输入。排序标准是：

1：按名字排序
2：然后按年龄排序
3：然后按分数排序
优先级是名字>年龄>分数。

如果将以下元组作为程序的输入给出：

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
然后，程序的输出应该是：

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
提示：
如果向问题提供输入数据，则应假定它是控制台输入。我们使用 sort 来启用多个排序键。
1、分割组装
2、调用 sort（）排序

"""


class Question019:

    def __init__(self):
        pass

    def test_fun(self):
        lst = []
        # 1、分割组装
        while True:
            i = input("按格式输入需要排序的元组(name, age, score)：").split(",")
            # print(i)
            if not i[0]:
                break
            lst.append(tuple(i))
            # print(lst)

        # 循环调用 sort（）排序
        # print(len(lst),len(lst[0]))
        """
            对元组组成的列表进行排序，sort
            1、将lst中的元组依次放入x中，即x代表一个元组，临时名字
            2、x[0]、x[1]、x[2]依次分别代表元组里面的第一个、第二个、第二个元素
            3、含义是按照列表中的顺序依次进行排序，前面的优先级大于后面的0>1>2,lambda是匿名函数
        """
        lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))
        print(lst)

if __name__ == "__main__":
    Question019().test_fun()