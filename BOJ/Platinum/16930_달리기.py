# 20241124
# 47:55
# 1 / 5

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


N, M, K = map(int, input().split())
area = [list(str(input())) for _ in range(N)]

si, sj, ei, ej = map(lambda inp:int(inp) - 1, input().split())
visited = [[0] * M for _ in range(N)]
visited[si][sj] = 1
queue = deque()
queue.append((si, sj))
while queue:
    ci, cj = queue.popleft()
    distance = visited[ci][cj]
    if ci == ei and cj == ej:
        print(distance - 1)
        exit()

    for d_idx, (di, dj) in enumerate(direction):
        for dd in range(1, K + 1):
            ni, nj = ci + di * dd, cj + dj * dd
            if ni < 0 or N <= ni or nj < 0 or M <= nj or area[ni][nj] == '#':
                break
            if visited[ni][nj]:
                if visited[ni][nj] <= distance:
                    break
                continue
            visited[ni][nj] = distance + 1
            queue.append((ni, nj))

print(-1)
