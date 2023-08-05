
# Task 1:
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#
print("Task 1 Arithmetic progression:")
a = int(input('Enter first element (a): '))
n = int(input('Enter amount of numbers (n): '))
d = int(input('Enter difference (d): '))
list_res = []
for i in range (n):
    list_res.append(a + (i) * d)
print (list_res)





