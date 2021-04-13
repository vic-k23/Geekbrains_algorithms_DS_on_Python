# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# Check sequence: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def get_prime_sieve(n):
    sieve = [2, 3, 5, 7]
    sieve.extend([i for i in range(4, n * 7) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0])

    for i in range(4, len(sieve)):
        for j in range(i + 1, len(sieve)):
            if sieve[i] != 1 and sieve[j] % sieve[i] == 0:
                sieve[j] = 1

    primes_list = [p for p in sieve if p != 1]
    while len(primes_list) <= n:
        range_left = primes_list[len(primes_list) - 1] + 1
        range_right = range_left + 3 * (n - len(primes_list))
        sieve = [i for i in range(range_left, range_right) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
        sieve = primes_list + sieve

        for i in range(4, len(sieve)):
            begin = i + 1 if i > len(primes_list) else len(primes_list)
            for j in range(begin, len(sieve)):
                if sieve[i] != 1 and sieve[j] % sieve[i] == 0:
                    sieve[j] = 1

        primes_list = [p for p in sieve if p != 1]

    return primes_list[n - 1]

# Время выполнения 100 запусков для поиска 200-го простого числа: 0.2798459 0.2788218 0.2794914
# Время выполнения 100 запусков для поиска 300-го простого числа: 0.6581132 0.6460709 0.6522496
# =====================================================================================================================
# Время выполнения 100 запусков для поиска 400-го простого числа: 1.1535372 1.1562736 1.1591388
# 648 function calls in 0.012 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 hw02.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 hw02.py:17(<listcomp>)
#         1    0.012    0.012    0.012    0.012 hw02.py:8(get_prime_sieve)
#         1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#       641    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# =====================================================================================================================
# Время выполнения 100 запусков для поиска 500-го простого числа: более 10 мин не дождался.
# Последнее число, которое удалось дождаться, идёт под номером 436, за время: 1.3918314999999999 1.4843531 1.3786671


def get_prime(n):
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n >= len(primes_list):
        p_dgt = 23
        # [fix] #2
        list_length = len(primes_list)
        while list_length <= n:
            p_dgt += 1
            i = 0

            # while i < len(primes_list):
            # [fix] #1
            list_end = len(primes_list)
            while i < list_end:
                if p_dgt % primes_list[i] == 0:
                    break
                i += 1
            else:
                primes_list.append(p_dgt)
                # [fix] #2
                list_length = len(primes_list)

    return primes_list[n - 1]

# Время выполнения 100 запусков для поиска 200-го простого числа: 0.29215040000000003 0.349511 0.3261449
# Время выполнения 100 запусков для поиска 300-го простого числа: 0.7043621999999999 0.9333202 1.0494894000000001
# ==================================================================================================================
# Время выполнения 100 запусков для поиска 400-го простого числа: 1.453028 1.3119589 1.6498226
# 88686 function calls in 0.030 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.030    0.030 <string>:1(<module>)
#         1    0.022    0.022    0.030    0.030 hw02.py:39(get_prime)
#         1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
#     88290    0.008    0.000    0.008    0.000 {built-in method builtins.len}
#       392    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ###################################################################################################################
# После внесения изменений во вложенный цикл while:
# 5850 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 hw02.py:56(get_prime)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      5454    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       392    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ##################################################################################################################
# Вторая доработка.
# 3516 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.005    0.005    0.005    0.005 hw02.py:56(get_prime)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#      3120    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       392    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===================================================================================================================
# Время выполнения 100 запусков для поиска 500-го простого числа: 2.229883 2.1120623000000003 2.513204
# Время выполнения 100 запусков для поиска 1000-го простого числа: 12.1174594 10.3504628 10.0952127 9.737768599999999


# def test_get_prime():
#     check_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
#                   103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
#
#     for i, num in enumerate(check_list):
#         assert num == get_prime(i + 1)
#     for i, num in enumerate(check_list):
#         assert num == get_prime_sieve(i + 1)


# print(test_get_prime())

if __name__ == '__main__':

    import timeit
    import cProfile

    n = 400

    print(timeit.timeit(f"get_prime({n})", setup="from __main__ import get_prime", number=100))
    # print(timeit.timeit(f"get_prime_sieve({n})", setup="from __main__ import get_prime_sieve", number=100))
    #
    cProfile.run('get_prime(n)')
    # cProfile.run('get_prime_sieve(n)')

"""
    Выводы.
    1. Во втором алгоритме очень много раз вызывается метод len. Очевидно, это происходит в цикле while. Можно уменьшить
        количество вызовов, используя переменную для хранения единожды вычисленного значения длины списка, которая,
        очевидно, не меняется, в теле вложенного цикла while. Такая поправка позволила в 3+ раза сократить время 
        выполнения функции  - до 0.4912465999999999 с вместо 1.3119589 (лучший результат для тех же параметров запуска).
        Пойдём дальше: будем вычислять длину списка только, если добавили элемент, иначе нет смысла этого делать.
        Новый результат: 0.4884611, что, в общем-то, не удивительно, так как эта доработка не сильно уменьшила кол-во
        вызовов встроенной функции len.
    2. Сложность алгоритмов: первый (на основе "решета"), похоже, имеет сложность О(2 ** n), так как в определённый 
        момент вермя выполнения улетает в бесконечность; второй, скорее всего, O(n), так как время выполнения 
        увеличивается пропорционально количеству вычисляемых элементов последовательности.
"""
