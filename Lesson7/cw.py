# Shell sorting algorithm
import random
from random import randint


def shell_sort(arr):

    def get_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    for step in get_increment(arr):
        for i in range(step, len(arr)):
            for j in range(i, step - 1, -step):
                if arr[j - step] <= arr[j]:
                    break
                arr[j], arr[j - step] = arr[j - step], arr[j]


def hoar_sort_no_ad_mem(array, bgn, end):
    if bgn >= end:
        return

    pivot = array[randint(bgn, end)]

    print(array, ' ', pivot)

    i, j = bgn, end

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    hoar_sort_no_ad_mem(array, bgn, j)
    hoar_sort_no_ad_mem(array, i, end)


size = 10

ar = [randint(0, 100) for _ in range(size)]
print(ar)
# shell_sort(ar)
hoar_sort_no_ad_mem(ar, 0, size - 1)
print(ar)
