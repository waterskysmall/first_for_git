# 类似c语言中的循环遍历数组，python中也可以循环遍历列表

list1=["仙贝",114514,"pycharm"]
for x in range(0,3):
    print(list1[x])

# 看我搞一个矩阵出来

a=[[1,2,3],[4,5,6],[7,8,9]]
for x in range(0,3):
    for y in range(0,3):
        print(a[x][y],end=" ")
    print()
#rt,完全可以用嵌套解释，列表中嵌套列表，其中元素若为列表也可以使用内置方法
#eg.1
# b=a[1].index(5)
# print(f"a列表中{b}")
#eg.2
# b=a.index([4,5,6])
# print(f"a列表中{b}")

#这下看懂了，不止可以直接搞一个列表，还可以用接受列表变量的

mylist=[1,2,3,4,5,5]
yourlist=[1,1,4,5,1,4]
mylist.extend(yourlist)
print(mylist)
weizhi=mylist.index(31)
print(f"31在mylist列表中在第{weizhi}个位置")