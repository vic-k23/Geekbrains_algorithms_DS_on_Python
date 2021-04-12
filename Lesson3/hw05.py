# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint


size = 20
range_border = 10
m = [randint(-1 * range_border, range_border) for _ in range(size)]
print(m)

max_negative = (-1) * range_border
# Bonus
min_positive = range_border
for i, d in enumerate(m):
    if 0 > d > max_negative:
        max_negative = d
    # Bonus
    elif 0 < d < min_positive:
        min_positive = d

print(f"Максимальный отрицательный элемент: {max_negative}")
# Bonus
print(f"Минимальный положительный элемент: {min_positive}")
