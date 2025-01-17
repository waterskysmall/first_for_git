import random
num=random.randint(1,10)
cai=int(input("猜一下1到10之间生成的数字："))
if cai<num:
    print("小了")
    cai=int(input("再猜一下："))
    if cai<num:
        print("小了")
        cai = int(input("最后一次机会咯："))
        if cai < num:
            print("小了，还是猜错了")
        elif cai > num:
            print("大了，还是猜错了")
        else:
            print("恭喜你猜中咯！")
    elif cai>num:
        print("大了")
        cai = int(input("最后一次机会咯："))
        if cai < num:
            print("小了，还是猜错了")
        elif cai > num:
            print("大了，还是猜错了")
        else:
            print("恭喜你猜中咯！")
    else :
        print("恭喜你猜中咯！")
elif cai>num:
    print("大了")
    cai = int(input("再猜一下："))
    if cai < num:
        print("小了")
        cai = int(input("最后一次机会咯："))
        if cai < num:
            print("小了，还是猜错了")
        elif cai > num:
            print("大了，还是猜错了")
        else:
            print("恭喜你猜中咯！")
    elif cai > num:
        print("大了")
        cai = int(input("最后一次机会咯："))
        if cai < num:
            print("小了，还是猜错了")
        elif cai > num:
            print("大了，还是猜错了")
        else:
            print("恭喜你猜中咯！")
    else:
        print("恭喜你猜中咯！")
else :
    print("恭喜你猜中咯！")
