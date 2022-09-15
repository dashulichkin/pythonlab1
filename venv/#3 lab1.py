#3.	Найдите сумму отрицательных элементов списка.
#Найдите сумму элементов списка между двумя
#первыми нулями. Если двух нулей нет в списке,
#то выведите ноль.
my_list = [1, -2, 0, 2, 2, -1, 1, 0, -6, 8, 10, 0]
print("Список:", my_list)
print()
sum = 0
for i in my_list:
    if i < 0:
        sum = sum +i
print("Сумма отрицательных элементов:",sum)
print()

kol = 0
for i in my_list:
    if i == 0:
        kol += 1
print("Количество нулей в списке:", kol)
print()

if kol >= 2:
    item = 0
    i = my_list.index(item)
    print("Индекс первого нуля:", i)

    start = i + 1
    i1 = my_list.index(item, start)
    print("Индекс второго нуля:", i1)
    if i1 == i + 1:
        print("Нули стоят рядом")
    else:
        new_my_list = my_list[i+1:i1]
        print()
        print("Элементы между двумя первыми нулями:")
        print(new_my_list)
        print()

        length = len(new_my_list)
        sum_of_elements = 0
        for i in range(length):
            sum_of_elements = sum_of_elements + new_my_list[i]
        print("Сумма элементов между двумя первыми нулями:", sum_of_elements)
else: #нулей нет, один ноль
    print("0")
