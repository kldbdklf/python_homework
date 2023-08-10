
# Task 1:
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


print('Task 1 Winnie the Pooh:')
VOWELS = 'ауоыиэяюёе'
Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
def Calculate_rhythm (song):
    rhythm = sum([1 for item in song[0] if item in VOWELS])
    for i in song:
        number_vowels = 0
        for j in i:
            if j in VOWELS:
                number_vowels += 1
        if number_vowels != rhythm:
            return False
    return True
song = input('Enter song: ')
song = song.lower()
if len([0 for item in song if item not in Alphabet]) == 0:
    song = song.split()
    if Calculate_rhythm(song):
        print('Парам пам-пам')
    else:
        print('Пам парам')
else:
    print('Your song must be in Russian')
