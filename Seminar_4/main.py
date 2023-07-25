"""
Task 1:
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""
import random

print("Task 1 Two lists: ")
n = int(input("Enter length of first list: "))
m = int(input("Enter length of second list: "))

def fill_list_manually(n):
    res_list = []
    for i in range(n):
        res_list.append(int(input(f"Enter {i + 1} number  of list: ")))
    return res_list
print("Fill first list: ")
n_list = fill_list_manually(n)
print("Fill second list: ")
m_list = fill_list_manually(m)
list_3 = [x for x in n_list if x in m_list]
set1 = sorted(set(list_3))
print(set1)

"""
Task 2:
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, 
поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""
print("Task 2 Garden bed: ")
def fill_list_random(n):
    res_list = []
    for i in range(n):
        res_list.append(random.randint(0,101))
    return res_list
size_garden_bed = int(input("Enter size of garden bed: "))
garden_bed = fill_list_random(size_garden_bed)
print(garden_bed)
max_yield = 0
best_bush = 0
for i in range(size_garden_bed):
    if garden_bed[i % size_garden_bed]\
            + garden_bed[(i - 1) % size_garden_bed]\
            + garden_bed[(i + 1) % size_garden_bed]\
            > max_yield:
        max_yield = garden_bed[i % size_garden_bed] \
                    + garden_bed[(i - 1) % size_garden_bed] \
                    + garden_bed[(i + 1) % size_garden_bed]
        best_bush = i
print(f'The best is bush № {best_bush + 1} with the maximum yield = {max_yield} berries')
