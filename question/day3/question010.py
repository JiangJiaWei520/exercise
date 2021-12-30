"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md
问题 10
问题
编写一个程序，接受一系列以空格分隔的单词作为输入，并在删除所有重复单词并按字母数字排序后打印这些单词。

假设向程序提供以下输入：

hello world and practice makes perfect and hello world again
然后，输出应该是：

again and hello makes perfect practice world
提示：
如果向问题提供输入数据，则应假定它是控制台输入。我们使用 set 自动删除重复数据，然后使用 sorted() 对数据进行排序。
set也是一组数，无序，内容又不能重复，通过调用set()方法创建
split() 排序 无返回值
"""
class Question010:
    def __init__(self):
        pass

    def test_fun(self):
        setlist = list(set(input("请以空格分隔的单词作为输入:").split(" ")))
        setlist.sort()
        print(setlist)


if __name__ == "__main__":
    Question010().test_fun()