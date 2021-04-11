# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


from random import randint
from hw03 import get_min_max


size = 20
rb = 10

m = [randint(1, rb) for _ in range(size)]
print(m)

borders = get_min_max(m)
frm = borders['min'][0] if borders['min'][1] < borders['max'][1] else borders['max'][0]
to = borders['min'][0] if borders['min'][1] > borders['max'][1] else borders['max'][0]

print(borders)

sum = 0

for i in range(frm + 1, to):
    sum += m[i]

print(f"Сумма чисел между {m[frm]} и {m[to]} равна {sum}")
