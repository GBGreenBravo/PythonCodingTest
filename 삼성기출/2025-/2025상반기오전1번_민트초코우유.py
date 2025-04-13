# 20250413
# 39:24
# 1 / 1

from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 북남서동


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or N <= xx


def breakfast():
    for i in range(N):
        for j in range(N):
            mind[i][j] += 1


def lunch():
    bosses = []

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                group = [(i, j)]
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx]:
                            continue
                        if food[ny][nx] != food[y][x]:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group.append((ny, nx))
                boss = max(group, key=lambda yx: (mind[yx[0]][yx[1]], -yx[0], -yx[1]))
                bosses.append(boss)
                for gy, gx in group:
                    if (gy, gx) == boss:
                        mind[gy][gx] += len(group) - 1
                    else:
                        mind[gy][gx] -= 1

    return bosses


def dinner(bosses):
    global defensing
    next_defensing = set()

    bosses.sort(key=lambda yx: (spread_order[food[yx[0]][yx[1]]], -mind[yx[0]][yx[1]], yx[0], yx[1]))
    for by, bx in bosses:
        if (by, bx) in defensing:
            continue

        dy, dx = direction[mind[by][bx] % 4]
        now_x = mind[by][bx] - 1
        mind[by][bx] = 1
        ny, nx = by + dy, bx + dx
        while not oob(ny, nx) and now_x > 0:
            if food[ny][nx] == food[by][bx] or (ny, nx) in defensing:
                ny, nx = ny + dy, nx + dx
                continue
            next_defensing.add((ny, nx))
            if now_x > mind[ny][nx]:
                now_x -= mind[ny][nx] + 1
                mind[ny][nx] += 1
                ny, nx = ny + dy, nx + dx
                continue
            else:
                mind[ny][nx] += now_x
                food[ny][nx] |= food[by][bx]
                break

    defensing = next_defensing


def print_mind():
    mind_statistics = [0] * 8
    for i in range(N):
        for j in range(N):
            mind_statistics[food[i][j]] += mind[i][j]
    result = []
    for i in print_order:
        result.append(mind_statistics[i])
    print(*result, sep=" ")


# 민트 1 / 초코 2 / 우유 4
# 초코우유 6 / 민트우유 5 / 민트초코 3
# 민트초코우유 7
food_sort = {"T": 1, "C": 2, "M": 4}
spread_order = [-1, 0, 0, 1, 0, 1, 1, 2]
print_order = (7, 3, 5, 6, 4, 2, 1)

N, T = map(int, input().split())
food = [[food_sort[str(i)] for i in input()] for _ in range(N)]
mind = [list(map(int, input().split())) for _ in range(N)]

defensing = set()

for _ in range(T):
    breakfast()
    dinner(lunch())
    print_mind()
