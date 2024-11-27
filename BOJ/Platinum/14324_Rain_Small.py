# 20241127
# 18:58
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or R <= yy or xx < 0 or C <= xx


T = int(input())
for test in range(1, T + 1):
    R, C = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(R)]

    origin_area = [row[:] for row in area]

    deque_list = [None] + [[] for _ in range(1000)]
    for i in range(R):
        for j in range(C):
            deque_list[area[i][j]].append((i, j))

    for height in range(1, 1001):
        for sy, sx in deque_list[height]:
            if area[sy][sx] != height:
                continue

            possible = 1001
            visited = [[0] * C for _ in range(R)]
            visited[sy][sx] = 1
            queue = deque()
            queue.append((sy, sx))
            group = [(sy, sx)]
            while queue and possible:
                y, x = queue.popleft()
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or area[ny][nx] < height:
                        possible = False
                        break
                    elif area[ny][nx] == height:
                        if visited[ny][nx]:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group.append((ny, nx))
                    else:
                        possible = min(possible, area[ny][nx])

            if possible:
                for gy, gx in group:
                    area[gy][gx] = possible
                deque_list[possible].extend(group)

        deque_list[height].clear()

    print(f"Case #{test}:", sum([area[row][col] - origin_area[row][col] for col in range(C) for row in range(R)]))
