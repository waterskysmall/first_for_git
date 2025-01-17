yu = 10000
for i in range(1, 21):
    import random

    num = random.randint(1, 10)
    # print(f"员工{i},绩效分{num},",end='')
    if yu > 0:
        if num < 5:
            print(f"员工{i},绩效分{num},", end='')
            print("绩效这么低还想要工资？下一位！")
            continue
        else:
            yu -= 1000
            print(f"发给员工{i}工资1000蚊子，账户还剩{yu}蚊子")
    else:
        print("不好意思喔，没钱了，下个月再来吧")
        break
