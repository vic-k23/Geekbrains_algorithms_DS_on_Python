# В разборе домашнего задания мне очень понравилась идея со специальным классом для оценки расхода памяти данными
# приложения. Такой класс вполне может пригодится в будущем в реальных проектах. Решил сделать черновой вариант такого
# класса.

from sys import getsizeof


class MemoryUsageAnalyzer:

    def __init__(self):
        self._total_memory = 0
        self._types = {}

    def __repr__(self):
        return "MemoryUsageAnalyzer()"

    def __str__(self):
        print_string = [f"Object use of memory in total: {self._total_memory} bytes"]
        for cls, usage in self._types.items():
            print_string.append(f"\t{usage[0]} objects of {cls} use {usage[1]} bytes")
        return "\n".join(print_string)

    def _add(self, obj):
        obj_mem_usage = getsizeof(obj)
        obj_cls_name = str(obj.__class__)

        self._total_memory += obj_mem_usage

        if obj_cls_name in self._types:
            self._types[obj_cls_name][0] += 1
            self._types[obj_cls_name][1] += obj_mem_usage
        else:
            self._types[obj_cls_name] = [1] * 2
            self._types[obj_cls_name][1] = obj_mem_usage

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for itm in obj.items():
                    self._add(itm)
            elif not isinstance(obj, str):
                for el in obj:
                    self._add(el)

    def analyze(self, *args, prt=False):
        for arg in args:
            self._add(arg)
        if prt:
            print(self.__str__())


if __name__ == '__main__':
    from random import randint

    size = 10000

    m = [randint(1, 300) for _ in range(size)]

    evens_indexes = {}

    for i, d in enumerate(m):
        if d % 2 == 0:
            evens_indexes[i] = d

    analyzer = MemoryUsageAnalyzer()

    analyzer.analyze(size, m, evens_indexes, prt=True)
