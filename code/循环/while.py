i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(f"1累加到100的和为{sum}")




import random
num=random.randint(1,100)
i=1
ci=0
while i:
    cai=int(input("猜一下1到100之间的整数，猜对了没奖励，猜错了有惩罚："))
    ci+=1
    if cai==num:
        print("恭喜你猜对咯，你猜了%d次就猜中了，有实力"%ci)
        i=0
    else :
        if cai>num:
            print("猜大了")
        else :
            print("猜小了")
