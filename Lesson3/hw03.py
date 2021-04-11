# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint


def get_min_max(arr):
    """
    Функция возвращает словарь минимального и максимального значения с их позициями в массиве
    :param arr: массив, в котором нужно найти максимально и минимальное значение
    :return: словарь минимального и максимального значения с их позициями в массиве
    """
    res = {'min': (0, arr[0]), 'max': (0, arr[0])}
    for i, a in enumerate(arr):
        if a > res['max'][1]:
            res['max'] = (i, a)
        elif a < res['min'][1]:
            res['min'] = (i, a)
    return res


if __name__ == "__main__":

    size = 30
    m = [randint(-10, 10) for _ in range(size)]
    print(m)

    min_max = get_min_max(m)
    print(min_max)

    m[min_max['min'][0]], m[min_max['max'][0]] = m[min_max['max'][0]], m[min_max['min'][0]]

    print(m)
