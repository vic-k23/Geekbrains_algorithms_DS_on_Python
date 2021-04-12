# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint


size = 100
m = [randint(1, 20) for _ in range(size)]
print(m)
counter_set = {}
for d in m:
    if d in counter_set.keys():
        counter_set[d] += 1
    else:
        counter_set[d] = 1

print(counter_set)

often = 0
for item in counter_set:
    if counter_set[item] > counter_set.get(often, 0):
        often = item

print(f"Наиболее часто встречающееся число: {often}")
