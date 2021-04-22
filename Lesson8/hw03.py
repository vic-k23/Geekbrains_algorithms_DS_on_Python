# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).

from random import randint


def generate_graph(n):
    """
    Функция генерации не взвешенного ориентированного графа с n вершинами
    :param n: количество вершин
    :return: матрица связности nxn представляющая граф
    """
    g = [[randint(0, 1) if i != j else 0 for j in range(n)] for i in range(n)]
    return g


def dfs(graph, start, is_visited=[]):

    length = len(graph)

    if len(is_visited) == 0:
        is_visited = [False] * length

    is_visited[start] = True
    path = [start]

    for i, edge in enumerate(graph[start]):
        if edge != 0 and not is_visited[i]:
            branch = dfs(graph, i, is_visited)
            if len(branch) > 1:
                path.append(branch)
            else:
                path += branch

    return path


def print_path(tree, level=1):

    print("|", "-" * level, end='')
    for node in tree:
        if type(node).__name__ == int.__name__:
            print(f"({node})", end=', ')

    print()

    for node in tree:
        if type(node).__name__ == list.__name__:
            print_path(node, level + 1)


if __name__ == '__main__':
    grph = generate_graph(20)
    # grph = [[0, 1, 0, 0, 0],
    #         [0, 0, 1, 1, 1],
    #         [0, 1, 0, 1, 1],
    #         [0, 0, 1, 0, 0],
    #         [1, 0, 0, 1, 0]]
    print(*grph, sep='\n')
    print('_' * 30)
    graph_tree = dfs(grph, 0)
    print(graph_tree)
    print_path(graph_tree)
