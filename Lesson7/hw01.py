# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

# 1000 loops, best of 5: 1.05 msec per loop, len(array) = 100
# 1000 loops, best of 5: 69 msec per loop, len(array) = 1000
def bubble_sort(array, ascending=True):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if (ascending and array[j - 1] > array[j]) or (not ascending and array[j - 1] < array[j]):
                array[j], array[j - 1] = array[j - 1], array[j]


# 1000 loops, best of 5: 719 usec per loop, len(array) = 100
# 1000 loops, best of 5: 36.3 msec per loop, len(array) = 1000
def bubble_sort_v2(array, ascending=True):
    for i in range(len(array) - 1):
        stop = len(array) - i - 1
        for j in range(stop):
            if (ascending and array[j] > array[stop]) or (not ascending and array[j] < array[stop]):
                array[j], array[stop] = array[stop], array[j]


def time_testing(num):
    from random import randint
    a = [randint(-100, 100) for _ in range(num)]
    bubble_sort(a, ascending=False)


if __name__ == '__main__':
    from random import randint

    size = 15

    ar = [randint(-100, 100) for _ in range(size)]
    print(ar)
    bubble_sort_v2(ar, ascending=False)
    print(ar)
