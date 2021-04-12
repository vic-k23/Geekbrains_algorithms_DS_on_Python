# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint


size = 15
rb = 10
m = [randint(1, rb) for _ in range(size)]
print(m)

min_pair = [rb, rb]
for d in m:
    if d < min_pair[0]:
        min_pair[1] = min_pair[0]
        min_pair[0] = d
    elif d == min_pair[0] or d < min_pair[1]:
        min_pair[1] = d

print(f"Два нименьших числа в массиве: {min_pair[0]} и {min_pair[1]}")
