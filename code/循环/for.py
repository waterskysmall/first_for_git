# 字母统计练习
# i=0
# name="itheima is a brand of itcast"
# for x in name:
#     if x=='a':
#         i+=1
# print(f"name中有{i}个a字母")

# 偶数统计练习
# num=0
# for x in range(1,100):
#     if x%2==0:
#         num+=1
# print("1到100之间有%d个偶数" %num)

# 测试临时变量作用域和c的区别，最好别这么用，要用临时变量可以在循环开始之前就定义，这样就可以取出循环终止之后的最后一个数值
# for x in range(1,114515):
#     if x==114514:
#         print(x)
# print("拖点时间")
# print("拖点时间")
# print("拖点时间")
# print("拖点时间")
# print("拖点时间")
# print("拖点时间")
# print(x)

# for99乘法
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end='')
    print()
