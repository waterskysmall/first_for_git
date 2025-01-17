lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listb = []
print(f"lista的内容为{lista},listb的内容为{listb}")
index = 1
while index < len(lista):
    element = lista[index]
    listb.append(element)
    index += 2
print(f"listb的内容为{listb}")
listb = []
element=0
for element in lista:
    if element % 2 != 0:
        continue
    listb.append(element)
print(f"listb的内容为{listb}")
