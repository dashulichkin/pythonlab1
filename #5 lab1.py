#5.	Реализуйте программу «Магазин автозапчастей», которая будет включать в себя шесть пунктов меню.
# У вас есть словарь, где ключ – название продукции.
# Значение – список, который содержит состав продукции,
# цену и кол-во (шт),которое есть в магазине.
#1.	Просмотр описания: название – описание
#2.	Просмотр цены: название – цена.
#3.	Просмотр количества: название – количество.
#4.	Всю информацию.
#5.	Покупка
#В пункте «Покупка» необходимо совершить покупку,  с клавиатуры вводите название продукции и его кол-во,
# n – выход из программы. Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке
#6.	До свидания

print('МЕНЮ МАГАЗИНА:')
print('1. Просмотр описания')
print('2. Просмотр цены')
print('3. Просмотр количества')
print('4. Всю информацию')
print('5. Покупка')
print('6. До свидания!')
print('Ваш выбор:')
s = int(input())

auto_shop = {'тормозные диски': ['алюминий', 200, 2],
             'колодки': ['металлическая пластина + фрикционная накладка', 500, 1],
             'подшипники': ['нержавеющая сталь', 100, 4],
             'жидкость для двигателя': ['масло', 50, 7]}

for key, value in auto_shop.items():
    if s == 1:
        print("{} - {}".format(key, value))

for key, value in auto_shop.items():
    if s == 2:
        print("{} - {}$".format(key, value[1]))

for key, value in auto_shop.items():
    if s == 3:
        print("{} - {} шт.".format(key, value[2]))

for key, value in auto_shop.items():
    if s == 4:
        print("{} - {}, {}$, {}шт.".format(key, value[0], value[1], value[2]))


def check_the_product():
    purchase = input('Введите название товара, который вы хотите приобрести: ')
    if purchase in auto_shop.keys():
        if purchase == 'тормозные диски':
            list1 = auto_shop.get('тормозные диски')
            print(f"В наличии осталось {list1[2]} шт.")
            print('Желаете приобрести товар?')
            answer = input()
            if answer == 'да':
                kol_purchase = int(input('Введите количество товара: '))
                if kol_purchase <= list1[2]:
                    print('Стоимость покупки составит: {}$'.format(kol_purchase * list1[1]))
                else:
                    print('Введенное количество превышает допустимое значение !')
            price = kol_purchase * list1[1]

        if purchase == 'колодки':
            list2 = auto_shop.get('колодки')
            print(f"В наличии осталось {list2[2]} шт.")
            print('Желаете приобрести товар?')
            answer = input()
            if answer == 'да':
                kol_purchase = int(input('Введите количество товара: '))
                if kol_purchase <= list2[2]:
                    price = print('Стоимость покупки составит: {}$'.format(kol_purchase * list2[1]))
                else:
                    print('Введенное количество превышает допустимое значение !')
            price = kol_purchase * list2[1]

        if purchase == 'подшипники':
            list3 = auto_shop.get('подшипники')
            print(f"В наличии осталось {list3[2]} шт.")
            print('Желаете приобрести товар?')
            answer = input()
            if answer == 'да':
                kol_purchase = int(input('Введите количество товара: '))
                if kol_purchase <= list3[2]:
                    price = print('Стоимость покупки составит: {}$'.format(kol_purchase * list3[1]))
                else:
                    print('Введенное количество превышает допустимое значение !')
            price = kol_purchase * list3[1]

        if purchase == 'жидкость для двигателя':
            list4 = auto_shop.get('жидкость для двигателя')
            print(f"В наличии осталось {list4[2]} шт.")
            print('Желаете приобрести товар?')
            answer = input()
            if answer == 'да':
                kol_purchase = int(input('Введите количество товара: '))
                if kol_purchase <= list4[2]:
                    price = print('Стоимость покупки составит: {}$'.format(kol_purchase * list4[1]))
                else:
                    print('Введенное количество превышает допустимое значение !')
            price = kol_purchase * list4[1]

            if answer == 'нет':
                check_the_product()
    else:
        print('Товар не найден!')

    print('Хотите добавить еще один товар?')
    answer_2 = input()
    while answer_2 != 'нет':
        def new_purchase():
            purchase_2 = input('Введите название товара, который вы хотите добавить: ')
            if purchase_2 in auto_shop.keys():
                if purchase_2 == 'тормозные диски':
                    print('В наличии осталось {} шт.'.format(list1[2]))
                    kol_purchase_2 = int(input('Введите количество товара: '))
                    if kol_purchase_2 <= list1[2]:
                        price_2 = print('Стоимость покупки составит: {}$'.format(price + kol_purchase_2 * list1[1]))
                price_2 = price + kol_purchase_2 * list1[1]

                if purchase_2 == 'колодки':
                    print('В наличии осталось {} шт.'.format(list2[2]))
                    kol_purchase_2 = int(input('Введите количество товара: '))
                    if kol_purchase_2 <= list2[2]:
                        price_2 = print('Стоимость покупки составит: {}$'.format(price + kol_purchase_2 * list2[1]))
                price_2 = price + kol_purchase_2 * list2[1]

                if purchase_2 == 'подшипники':
                    print('В наличии осталось {} шт.'.format(list3[2]))
                    kol_purchase_2 = int(input('Введите количество товара: '))
                    if kol_purchase_2 <= list3[2]:
                        price_2 = print('Стоимость покупки составит: {}$'.format(price + kol_purchase_2 * list3[1]))
                price_2 = price + kol_purchase_2 * list3[1]

                if purchase_2 == 'жидкость для двигателя':
                    print('В наличии осталось {} шт.'.format(list4[2]))
                    kol_purchase_2 = int(input('Введите количество товара: '))
                    if kol_purchase_2 <= list4[2]:
                        price_2 = print('Стоимость покупки составит: {}$'.format(price + kol_purchase_2 * list4[1]))
                price_2 = price + kol_purchase_2 * list4[1]

    if answer_2 == 'нет':
        print(f'Стоимость покупки - {price}')

for key, value in auto_shop.items():
    if s == 5:
        check_the_product()

