# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


m = []
for row in range(5):
    m.append([])
    summ = 0
    for col in range(3):
        m[row].append(int(input(f"Введите элемент {col} строки {row}: ")))
        summ += m[row][col]
    m[row].append(summ)

for row in m:
    for itm in row:
        print(f"{itm:>5}", end='')
    print()
