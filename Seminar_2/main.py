"""
Task 1:
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random

print("Task 1 \"Coins\": ")
number_of_coins = int(input("Enter number of coins: "))
temp = 0
eagles = 0
for i in range(number_of_coins):
    temp = random.randint(0,1)
    # print(temp, end = ' ') Для проверки
    if temp == 1:
        eagles += 1
print()
if (number_of_coins - eagles > eagles):
    print(f"You need to turn over {eagles} coins!")
else:
    print(f"You need to turn over {number_of_coins - eagles} coins!")




