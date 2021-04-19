# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Возьмём задачу на нахождение индексов чётных чисел в заданном массиве.

# Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32

from sys import getsizeof


def show_sizeof(x, level=0, verbose=True):
    if verbose:
        print("\t" * level, x.__class__, getsizeof(x), x)
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for xx in x.items():
                    show_sizeof(xx, level + 1)
            else:
                for xx in x:
                    show_sizeof(xx, level + 1)
    else:
        print(x.__class__, getsizeof(x))

# Variant 1


@profile
def get_evens_indexes_v1(m):
    evens_indexes = []
    # show_sizeof(evens_indexes, verbose=False)

    for i, d in enumerate(m):
        if d % 2 == 0:
            evens_indexes.append(i)
            # print(f"{i}, ", end='')

    # show_sizeof(evens_indexes, verbose=False)
    return evens_indexes


"""
Time of 100 runs: 0.6435634 0.6373375

Filename: .\Lesson6\hw01.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27   20.152 MiB   20.152 MiB           1   @profile
    28                                         def get_evens_indexes_v1(m):
    29   20.152 MiB    0.000 MiB           1       evens_indexes = []
    30                                             # show_sizeof(evens_indexes, verbose=False)
    31
    32   20.348 MiB    0.004 MiB       10001       for i, d in enumerate(m):
    33   20.348 MiB    0.098 MiB       10000           if d % 2 == 0:
    34   20.348 MiB    0.094 MiB        5067               evens_indexes.append(i)
    35                                                     # print(f"{i}, ", end='')
    36
    37                                             # show_sizeof(evens_indexes, verbose=False)
    38   20.348 MiB    0.000 MiB           1       return evens_indexes
"""

# Variant 2


@profile
def get_evens_indexes_v2(m):
    evens_indexes = [i for i, v in enumerate(m) if v % 2 == 0]

    # show_sizeof(evens_indexes, verbose=False)

    return evens_indexes


"""
Time of 100 runs: 0.6357636 0.6217701999999999

Filename: .\Lesson6\hw01.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    65   20.348 MiB   20.348 MiB           1   @profile
    66                                         def get_evens_indexes_v2(m):
    67   20.406 MiB    0.059 MiB       10003       evens_indexes = [i for i, v in enumerate(m) if v % 2 == 0]
    68
    69                                             # show_sizeof(evens_indexes, verbose=False)
    70
    71   20.406 MiB    0.000 MiB           1       return evens_indexes
"""

# Variant 3


@profile
def get_evens_indexes_v3(m):
    evens_indexes = {}
    # show_sizeof(evens_indexes, verbose=False)

    for i, d in enumerate(m):
        if d % 2 == 0:
            evens_indexes[i] = d

    # show_sizeof(evens_indexes, verbose=False)
    return evens_indexes.keys()


"""
Time of 100 runs: 0.629453 0.6236662000000001

Filename: .\Lesson6\hw01.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    93   20.406 MiB   20.406 MiB           1   @profile
    94                                         def get_evens_indexes_v3(m):
    95   20.406 MiB    0.000 MiB           1       evens_indexes = {}
    96                                             # show_sizeof(evens_indexes, verbose=False)
    97
    98   20.645 MiB    0.000 MiB       10001       for i, d in enumerate(m):
    99   20.645 MiB    0.000 MiB       10000           if d % 2 == 0:
   100   20.645 MiB    0.238 MiB        5067               evens_indexes[i] = d
   101
   102                                             # show_sizeof(evens_indexes, verbose=False)
   103   20.645 MiB    0.000 MiB           1       return evens_indexes.keys()    
"""

if __name__ == '__main__':
    from random import randint
    # import timeit
    # import cProfile

    size = 10000

    m = [randint(1, 300) for _ in range(size)]

    # print(show_sizeof(m))
    # print(m)

    # print("=" * 10, 'Version 1', '=' * 10)
    # show_sizeof(get_evens_indexes_v1(m), verbose=False)
    # print("=" * 10, 'Version 2', '=' * 10)
    # show_sizeof(get_evens_indexes_v2(m), verbose=True)
    # print("=" * 10, 'Version 3', '=' * 10)
    # show_sizeof(get_evens_indexes_v3(m), verbose=True)

    get_evens_indexes_v1(m)
    get_evens_indexes_v2(m)
    get_evens_indexes_v3(m)

"""
Вывод:
    Меньше всего памяти использует вариант №2, что, очевидно, связано с использованием генератора списка, вместо
    приращения списка в цикле, что приводит к избыточному выделению памяти при увеличении объёма резервируемой памяти
    под список.
"""

# print(timeit.timeit("get_evens_indexes_v1([randint(1, 50) for _ in range(10000)])",
#                      setup="from random import randint; from __main__ import get_evens_indexes_v1", number=100))
# print(timeit.timeit("get_evens_indexes_v2([randint(1, 50) for _ in range(10000)])",
#                      setup="from random import randint; from __main__ import get_evens_indexes_v2", number=100))
# print(timeit.timeit("get_evens_indexes_v3([randint(1, 50) for _ in range(10000)])",
#                      setup="from random import randint; from __main__ import get_evens_indexes_v3", number=100))
