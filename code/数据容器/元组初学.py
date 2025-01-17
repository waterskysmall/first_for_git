lista = ['football', 'music']
# 定义一个列表装在元组里面
tuple1 = ('牢大', 11, lista)
# 定义元组内部嵌套一个列表
location = tuple1.index(11)
# 定义变量location，通过内置的index方法找出元组中为11的下标赋值给location
print(f"年龄在元组中的下标位置为{location}")
print(f"学生的姓名为{tuple1[0]}")
del (lista[0])
# 删除列表中的元素football
print(f"删除完成，删除football爱好的元组为{tuple1}")
lista.insert(0, "coding")
# 使用列表方法insert插入元素coding为第一个元素，下标为0
print(f"加入爱好成功，加入coding爱好后元组的内容为{tuple1}")
