# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти.

from collections import deque

g = [[0, 0, 1, 1, 9, 0, 0, 0],
     [0, 0, 9, 4, 0, 0, 5, 0],
     [0, 9, 0, 0, 3, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 7, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 2, 0]]


def dejkstra_map(graph, departure):
    length = len(graph)
    start = departure
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    path = [deque() for _ in range(length)]

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        # Перераспределяем стоимость пути
        for i, vert in enumerate(graph[start]):
            if vert != 0 and not is_visited[i]:
                if cost[i] > vert + cost[start]:
                    cost[i] = vert + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        # Выбираем, куда идти дальше
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    # Строим пути
    for i in range(length):
        if i == departure or parent[i] == -1:
            continue
        k = i
        while k != departure:
            path[i].appendleft(k)
            if parent[k] >= 0:
                k = parent[k]
            else:
                break

        path[i].appendleft(departure)

    return [(cost[i], list(path[i])) for i in range(length)]


s = int(input("Where shall we start?"))

print(*dejkstra_map(g, s), sep='\n')
