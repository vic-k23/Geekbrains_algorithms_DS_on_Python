"""
Задание №3.
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
"""

from random import random, randint


a = input("Введите начало диапазона: ")
b = input("Введите конец диапазона: ")
generator = int(input("Выберите вариант генерации (1 - целое число, 2 - вещественное число, другое - маленькая буква \
латинского алфавита): "))

if generator == 1:
    print(randint(int(a) + 1, int(b)))
elif generator == 2:
    print(random() * (float(b) - float(a)) + float(a))
else:
    print(chr(randint(ord(a) + 1, ord(b))))
