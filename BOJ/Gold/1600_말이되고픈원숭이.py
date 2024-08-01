# 20240801
# 15:05
# 1 / 1

from collections import deque

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

monkey_move = ((0, 1), (0, -1), (1, 0), (-1, 0))
horse_move = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

queue = deque()
queue.append((0, 0, 0))  # y, x, used_k
visited[0][0][0] = 1


def oob(yy, xx):
    return not(0 <= yy < h) or not(0 <= xx < w)


while queue:
    y, x, used_k = queue.popleft()
    distance = visited[used_k][y][x] + 1

    for dy, dx in monkey_move:
        ny, nx = y + dy, x + dx
        if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
            visited[used_k][ny][nx] = distance
            queue.append((ny, nx, used_k))

    if used_k == k:
        continue
    used_k += 1
    for dy, dx in horse_move:
        ny, nx = y + dy, x + dx
        if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
            visited[used_k][ny][nx] = distance
            queue.append((ny, nx, used_k))


answers = [visit[h - 1][w - 1] for visit in visited if visit[h - 1][w - 1] != 0]
print(min(answers) - 1 if answers else -1)


# answers에 저장할 필요 없이, BFS이기 때문에 거리순으로 탐색하므로, 마지막 좌표 만나면 return 시키면 됨.
"""
from collections import deque

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

monkey_move = ((0, 1), (0, -1), (1, 0), (-1, 0))
horse_move = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]

queue = deque()
queue.append((0, 0, 0))  # y, x, used_k
visited[0][0][0] = 1


def oob(yy, xx):
    return not(0 <= yy < h) or not(0 <= xx < w)


def bfs():
    while queue:
        y, x, used_k = queue.popleft()
        if y == h - 1 and x == w - 1:
            return visited[used_k][y][x] - 1

        distance = visited[used_k][y][x] + 1

        for dy, dx in monkey_move:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
                visited[used_k][ny][nx] = distance
                queue.append((ny, nx, used_k))

        if used_k == k:
            continue
        used_k += 1
        for dy, dx in horse_move:
            ny, nx = y + dy, x + dx
            if not oob(ny, nx) and arr[ny][nx] != 1 and not visited[used_k][ny][nx]:
                visited[used_k][ny][nx] = distance
                queue.append((ny, nx, used_k))
    return -1


print(bfs())
"""