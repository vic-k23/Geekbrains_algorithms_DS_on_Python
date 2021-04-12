# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint


size = 5
rb = 100
m = [[randint(1, rb) for _ in range(size)] for _ in range(size)]

for row in m:
    for itm in row:
        print(f"{itm:>4}", end='')
    print()

min_items = [rb] * size
max_among_min = 0
for col in range(size):
    for row in range(size):
        if m[row][col] < min_items[col]:
            min_items[col] = m[row][col]
    if min_items[col] > max_among_min:
        max_among_min = min_items[col]

print('=' * 4 * size)
for itm in min_items:
    print(f"{itm:>4}", end='')
print()
print(f"максимальный элемент среди минимальных элементов столбцов матрицы: {max_among_min}")
