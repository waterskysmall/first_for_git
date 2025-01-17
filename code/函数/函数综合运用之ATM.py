yu = 500000
name = input("请输入用户名：")
print("----------------主菜单----------------")
print(f"{name},你好,欢迎来ATM,请选择操作：")
choose = int(input("查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]\n请输入你的选择："))


# if choose>4:
#     print("你个唐人，就瞎摁")
# elif choose<1:
#     print("别乱搞")

def fun1():
    global yu
    print("-------------查询余额------------\n%s,你好,你的余额剩余：%d元" % (name, yu))
    return int(input("查询余额\t[输入1]\n存款\t[输入2]\n取款\t[输入3]\n退出\t[输入4]\n请输入你下一步的需求："))


def fun2():
    global yu
    print(f"-------------存款------------\n{name},你好,你的余额剩余：{yu}元,请输入想存入的金额：")
    cun = int(input())
    yu += cun
    print("存款成功！你现在的余额为：%d元" % yu)
    return int(input("查询余额\t[输入1]\n存款\t[输入2]\n取款\t[输入3]\n退出\t[输入4]\n请输入你下一步的需求："))


def fun3():
    global yu
    print("-------------取款------------\n%s,你好,你的余额剩余：%d元,请输入想取出的金额：" % (name, yu))
    qu = int(input())
    if qu > yu:
        print("真是个人才，还想从这里空手套白狼。。。")
        return -1
    else:
        yu -= qu
        print("取款成功！你现在的余额为：%d元" % yu)
    return int(input("查询余额\t[输入1]\n存款\t[输入2]\n取款\t[输入3]\n退出\t[输入4]\n请输入你下一步的需求："))


def fun4():
    print("-------------退出成功！------------")


while choose != 4:
    if choose == 1:
        choose = fun1()
    elif choose == 2:
        choose = fun2()
    elif choose == 3:
        choose = fun3()
    else:
        print("数据非法！(取款大于余额或者不按要求输入选择)")
        break
if choose == 4:
    fun4()