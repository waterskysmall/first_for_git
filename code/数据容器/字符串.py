# 字符串是不可修改的数据容器
# 同之前学的列表和元组,字符串也有内置的方法,黑马举了几个例子:replace index split strip count方法
str1 = "114514仙贝"
# index:查找元素的位置(原来这玩意是找第一个出现括号里面的值并返回他的位置,后面的是找不到的)
location = str1.index("贝")  # 这样?python的中文字符占一个位置吗?
print(location)

# replace:要传入两个参数,把旧字符串的第一个参数的内容全部替换成第二个参数的内容
# 但旧字符串本身是没有改变的,可以定义一个新字符串接收修改后的内容
str2 = str1.replace("1", "牢")
print(f"replace前str1为{str1},replace后str1为{str1}")
print(f"replace后的结果由str2接收,str2为{str2}")

# split:传入一个字符串,将旧字符串按之分割(传入的那个字符串会消失)
# 分割而成的元素将存入一个列表中,所以可以定义一个列表存入分割后的字符串,但是注意旧字符串是没有改变的
str3 = "hi python itheima itcast"
str3list = str3.split("it")
print(str3list)

# strip:可传可不传,从字符串的首尾开始遍历,直到出现不等于传入的参数的字符就停下
# 如果没有传入参数,默认去除首位的空格和回车
str4 = "12hello world12"
newstr4 = str4.strip("12")  # 这里传入"12"的实际意义是传入"1"和"2",将首尾含这玩意的全都清除
print(newstr4)
print(str4)# rt原来的字符串是没有被修改的

# count:统计字符串中某元素出现的次数,传入一个字符串,返回一个int值,可设置变量接收
str5="hello world"
element=str5.count("he")
print(f"he在字符串str5中出现了{element}次")
