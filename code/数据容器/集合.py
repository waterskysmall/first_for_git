# 集合特点相较序列（列表，元组，字符串）有无序禁重的特点
# 集合内置有方法difference等，定义用花括号{}

# difference:从a中找出b中没有的元素，把他弄到一个新的集合去
a = {"1145", '仙贝', '想你了牢', '肘击男孩'}
b = {"仙贝", '牢 大', '1145', '疯狂原始人'}
c = a.difference(b)
print(c)

# difference_update:从a中找出b中有的元素,然后丢掉，只留下b中没有的元素，和difference的区别在修改了a的内容
a.difference_update(b)
print(a)

# clear:清空操作，在序列中也可用，直接会把集合清空，不需要传入参数
c.clear()
print(c)

# union:合并操作，将ab两集合直接合并，但是还是会查重，由于禁重的特点
# 有一个注意点，合并之后生成一个新集合要搞变量接收，不会改变原来ab集合的内容
c = a.union(b)
print(c)

# 最后还有一个老生常谈的len，这玩意序列里面也可以用，用来测量集合的长度，注意是查重之后的长度
# 会返回一个查找值，可以整一个变量接收
d = {324, 234, 324, 463, 345, 463}
element = len(d)
print(element)

# 集合遍历，通常来说不能用while，但是好像可以用，要点小方法
# 我先用for做一次看看
for i in d:
    print(i)
element = 0
while element < len(d):
    print(d.pop())
# 事实证明可以遍历，用点小方法就可以
