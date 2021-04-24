# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечаниe: в сумму не включаем пустую строку и строку целиком;

def count_substrings(s: str, verbose=False):

    s_length = len(s)
    substr_list = set()

    for i in range(s_length):
        for j in range(s_length - 1 if i == 0 else s_length, i, -1):
            sub = s[i:j]
            if verbose:
                print(sub)
            substr_list.add(hash(sub))

    return len(substr_list)


# print(count_substrings('hello'))
print(count_substrings('hello', True))
