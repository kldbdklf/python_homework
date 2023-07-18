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
    # print(temp, end = ' ') для проверки
    if temp == 1:
        eagles += 1
print()
if (number_of_coins - eagles > eagles):
    print(f"You need to turn over {eagles} coins!")
else:
    print(f"You need to turn over {number_of_coins - eagles} coins!")


"""
Task 2: 
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

print("Task 2 \"Two numbers\": ")
first_number = int(input("Enter first number = "))
second_number = int(input("Enter second number = "))
if first_number <= 1000 and second_number <= 1000:
    s = first_number + second_number
    p = first_number * second_number
    i = 1
    anti_duplication = 0
    while i < s and anti_duplication == 0:
        if (i * (s - i)) == p:
            print(f"Your first number = {i}, second number = {s - i} or your first number = {s - i}, second number = {i}")
            anti_duplication += 1
        i += 1
else:
    print("You are a little crook!")


"""
Task 3: 
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

print("Task 3 \"Degrees of 2\": ")
input_number = float(input("Enter your number = "))
if input_number >= 1:
    print("Degrees: ")
    degrees_of_two = 0
    while 2**degrees_of_two <= input_number:
        print(degrees_of_two, end = ' ')
        degrees_of_two += 1
else:
    print("There are no such powers, when raised to which the number 2, "
          "the result would be less than the entered number. "
          "There are no solutions!")