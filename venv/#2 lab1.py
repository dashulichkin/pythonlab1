#Посчитать, сколько пар (стоят рядом)
#верхнего и нижнего регистра находится в веденном с
#клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
#а также сколько всего букв в слове.
print("Введите слово")
wrd = input()
up_char = 0
low_char = 0
for i in range(len(wrd) - 1):
    if wrd[i].isupper() and wrd[i + 1].isupper():
        up_char += 1
    elif wrd[i].islower() and wrd[i + 1].islower():
        low_char += 1
print(f'Количество пар верхнего регистра: {up_char}\nКоличество пар нижнего регистра: {low_char}')
print("Количество букв в введенном слове:",len(wrd))