# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint


r = randint(0, 100)
for i in range(0, 10):
    g = int(input("Введите число от 0 до 100: "))
    if g == r:
        print("УГАДАЛ!")
        break
    elif g > r:
        print("Меньше!")
    else:
        print("Больше!")
if i == 9:
    print(f"Я загадал число {r}")
