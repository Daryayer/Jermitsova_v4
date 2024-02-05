from random import *

#4 вариант. 1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зверьков. Между двумя соседними зверьками также имеется пустой (из пробелов) столбец. 
#Разрешается вывести пустой столбец после последнего зверька. Для упрощения рисования скопируйте зверька из примера в среду разработки.

while True:
   try:
       kassidearv = int(input("Tere! Kui palju kassid sa tahad? Vali number 1-9:"))
       break
   except ValueError:
       print("See pole täisarv")
if kassidearv <1 or kassidearv >9:
   print("Vali õige number")
else:
   x = 0
   for x in range (kassidearv):
       print("  ^---^  ", end=" ")
   print("\n", end="")
   for x in range (kassidearv):
       print(" ( o o ) ", end=" ")
   print("\n", end="")
   for x in range (kassidearv):
       print("  ! = !/)", end=" ")
   print("\n")

#2 Вывести степени натуральных чисел, не превосходящие данного числа n*100. Пользователь задает показатель степени и число n.

while True:
   try:
       number = int(input("Tere! Sisesta number:"))
       kraad = int(input("Sisesta kraad:"))
       break
   except ValueError:
       print("See pole täisarv")
vastus = number**kraad
print("Siin on sinu vastus:", vastus)

#3 Известны оценки по физике каждого из учеников класса. Определить минимальную и максимальную оценки. (Оценки и количество учеников получаем случайным образом)

while True:
   try:
       kusimus = str(input("Tere! Kas sa tahad alustada programmi?  jah või ei: "))
       break
   except ValueError:
       print("Vali õige vastu")
if kusimus == "jah":
   hinnelist = []
   student = randint(1,30)
   for x in range (student):
       hinne = randint(1,100)
       print (hinne, end=", ")
       hinnelist.append (hinne)
   print("\n")
   print(max(hinnelist),"Maksimaalne hinne")
   print(min(hinnelist) ,"Minimaalne hinne")
else:
   print("Head aega!")

#4 Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет через 3, 6, 9, ..., 24 часа, если первоначально была одна амеба.

amoob = 1
while True:
   try:
       tere = str(input("Tere! Kas sa tahad alustada programmi?  jah või ei: "))
       break
   except ValueError:
       print("Vali õige vastu")
if tere == "jah":
   numb = 0
   while numb!=8:
       amoob = amoob*2
       print(amoob, end=" amyoobad parast kolm tundi, ")
       numb += 1
   print("\n Head aega")
else:
   print("Head aega")

  
