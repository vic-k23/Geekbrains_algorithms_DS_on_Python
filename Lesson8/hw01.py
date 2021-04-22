# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

# n = 5
n = int(input("How many friends met? "))

g = [_ for _ in range(n)]
num = 0
for vertex in range(n):
    g[vertex] = [0] * n
    for path in range(vertex + 1, n):
        g[vertex][path] = 1
        num += 1

print('Graph is:')
print(*g, sep='\n')
print(f"Number of handshakes is {num}")
