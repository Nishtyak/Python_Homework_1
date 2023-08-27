# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

print("Задача 1 (10)")
n = int(input("Введите количество монеток: "))
arr = []
for i in range(n):
    arr.append(random.randrange(2))
print(arr)

count0 = 0
count1 = 0
for item in arr:
    if item == 0:
        count0 += 1
    else:
        count1 += 1

result = count0 if count0 < count1 else count1
print(f"Минимальное число монеток, которые нужно перевернуть: {result}")
print()


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("Задача 2 (12)")
sum = int(input("Введите сумму чисел: "))
multy = int(input("Введите произведение чисел: "))

if sum > 2000:
    print("Загаданные числа меньше 1000!")
else:
    x = 1
    y = sum - x
    for i in range(int(sum / 2)):
        if x * y == multy:
            break
        else:
            x += 1
            y -= 1

    if x * y == multy:
        print(f"x = {x}, y = {y}")
    else:
        print("Таких чисел нет!")
print()


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

print("Задача 3 (14)")
n = int(input("Введите натуральное число n: "))

# if n < 1

arr = []
square = 1
i = 1
while square <= n:
    arr.append(square)
    square = 2 ** i
    i += 1

print(arr)

#update for merge