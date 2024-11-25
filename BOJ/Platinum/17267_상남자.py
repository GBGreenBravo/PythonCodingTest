# 20241125
# 1:33:26
# 1 / 13

from heapq import heappop, heappush

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def bfs():
    while queue:
        _, y, x, l, r = heappop(queue)

        ny = y + 1
        while True:
            if oob(ny, x) or visited[ny][x] or area[ny][x]:
                break
            visited[ny][x] = 1
            heappush(queue, (-l-r, ny, x, l, r))
            ny += 1

        ny = y - 1
        while True:
            if oob(ny, x) or visited[ny][x] or area[ny][x]:
                break
            visited[ny][x] = 1
            heappush(queue, (-l-r, ny, x, l, r))
            ny -= 1

        for ll in range(1, min(2, l + 1)):
            nx = x - ll
            if oob(y, nx) or visited[y][nx] or area[y][nx]:
                break
            visited[y][nx] = 1
            heappush(queue, (-l-r+ll, y, nx, l - ll, r))

        for rr in range(1, min(2, r + 1)):
            nx = x + rr
            if oob(y, nx) or visited[y][nx] or area[y][nx]:
                break
            visited[y][nx] = 1
            heappush(queue, (-l-r+rr, y, nx, l, r - rr))


N, M = map(int, input().split())
L, R = map(int, input().split())
area = [[int(i) for i in str(input())] for _ in range(N)]

visited = [[0] * M for _ in range(N)]
queue = []

for i in range(N):
    for j in range(M):
        if area[i][j] == 2:
            area[i][j] = 0
            visited[i][j] = 1
            heappush(queue, (-L-R, i, j, L, R))
            break
    else:
        continue
    break

bfs()

answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            answer += 1
print(answer)
