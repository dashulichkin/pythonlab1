#4.В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 6 очков;
#Q, Z – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова.

import re

print("Введите слово!")
def characters(word):
	return bool(re.search('[a-zA-Z]', word ))
dict = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

word = input().upper()
if characters(word):
	print(sum([k for i in word for k, v in dict.items() if i in v]))