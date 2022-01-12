"""
来源：https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md
问题67
问题
请编写一个二分搜索函数，在一个排序的列表中搜索一个项目。函数应该返回列表中要搜索的元素的索引。

提示
使用if/elif处理条件。
[1,2,3,4,5,6]
查找3
长度6/2=3
if [3]=4>3
    0-2
        3/2=1.5=1
            [1]=2<3
                2-2
                    找到3或者返回无数据

    3-5
"""
lst = [1, 2, 3, 4, 5, 6]
low = 0
high = len(lst)-1
# print(high)
i = int(input("输入要查到的值："))
while low <= high:
    mid = round((low+high)/2)

    if lst[mid] == i:
        print("要查找的值索引为：",mid)
        break
    elif lst[mid] > i:
        high = mid - 1
    elif lst[mid] < i:
        low = mid + 1
else:
    print("要查找的值不在范围内")