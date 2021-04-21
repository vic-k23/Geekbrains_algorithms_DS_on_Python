# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def merge_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return

    fst_part = array[:array_length // 2]
    snd_part = array[array_length // 2:]
    fst_part_len = len(fst_part)
    snd_part_len = len(snd_part)

    # print(fst_part)
    # print(snd_part)

    merge_sort(fst_part)
    merge_sort(snd_part)

    sorted_array = [0] * array_length
    one_index = two_index = 0

    for sorted_index in range(array_length):
        if one_index == fst_part_len or two_index == snd_part_len:
            break
        else:
            if fst_part[one_index] <= snd_part[two_index]:
                sorted_array[sorted_index] = fst_part[one_index]
                one_index += 1
            else:
                sorted_array[sorted_index] = snd_part[two_index]
                two_index += 1

    while one_index < fst_part_len and sorted_index < array_length:
        sorted_array[sorted_index] = fst_part[one_index]
        sorted_index += 1
        one_index += 1

    while two_index < snd_part_len and sorted_index < array_length:
        sorted_array[sorted_index] = snd_part[two_index]
        sorted_index += 1
        two_index += 1

    for i in range(array_length):
        array[i] = sorted_array[i]


if __name__ == '__main__':
    from random import random

    size = 10

    a = [random() * 49 for _ in range(size)]

    print(a)
    merge_sort(a)
    print(a)
