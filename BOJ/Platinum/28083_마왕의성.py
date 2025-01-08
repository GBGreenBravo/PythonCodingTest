# 20250109
# 22:30
# 1 / 1


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    height_a = height[a // M][a % M]
    height_b = height[b // M][b % M]
    if height_a > height_b:
        parent[b] = a
        parents_tax[a] += parents_tax[b]
    elif height_b > height_a:
        parent[a] = b
        parents_tax[b] += parents_tax[a]
    else:
        if a < b:
            parent[b] = a
            parents_tax[a] += parents_tax[b]
        else:
            parent[a] = b
            parents_tax[b] += parents_tax[a]


N, M = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(N)]
tax = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N * M)]
parents_tax = [tax[i // M][i % M] for i in range(N * M)]
answer = [[0] * M for _ in range(N)]

order = [(height[i][j], i, j) for j in range(M) for i in range(N)]
order.sort()

before_height = 0
candidates = []
for criteria, sy, sx in order:
    if criteria != before_height:
        for cy, cx in candidates:
            answer[cy][cx] = parents_tax[find(cy * M + cx)]
        before_height = criteria
        candidates = []

    candidates.append((sy, sx))
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = sy + dy, sx + dx
        if ny < 0 or N <= ny or nx < 0 or M <= nx:
            continue
        if height[sy][sx] >= height[ny][nx]:
            first = find(sy * M + sx)
            second = find(ny * M + nx)
            if first != second:
                union(first, second)
else:
    for cy, cx in candidates:
        answer[cy][cx] = parents_tax[find(cy * M + cx)]

for row in answer:
    print(*row)
