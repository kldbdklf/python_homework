import random
# Task 1:
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#
# print("Task 1 Arithmetic progression:")
# a = int(input('Enter first element (a): '))
# n = int(input('Enter amount of numbers (n): '))
# d = int(input('Enter difference (d): '))
# list_res = []
# for i in range (n):
#     list_res.append(a + (i) * d)
# print (list_res)

# Task 2:
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


print("Task 2 Indexes in the range:")
def fill_list_random(n):
    res_list = []
    for i in range(n):
        res_list.append(random.randint(0,10))
    return res_list
list_1 = fill_list_random(20)
print(list_1)
min_number = int(input('Enter min: '))
max_number = int(input('Enter max: '))
if (min_number < max_number):
    res_list2 = []
    for i in range(len(list_1)) :
        for j in range (min_number, max_number + 1):
            if j == list_1[i]:
                res_list2.append(i)
    print(res_list2)
else:
    print('Input incorrect! Your min_number must be less than the max_number.')