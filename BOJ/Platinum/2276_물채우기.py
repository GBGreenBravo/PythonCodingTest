# 20241209
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or M <= xx


def is_border(yy, xx):
    return yy < 1 or N - 1 <= yy or xx < 1 or M - 1 <= xx


M, N = map(int, input().split())
origin_area = [list(map(int, input().split())) for _ in range(N)]
area = [row[:] for row in origin_area]

for i in range(1, N - 1):
    for j in range(1, M - 1):
        near_heights = []
        for di, dj in direction:
            ni, nj = i + di, j + dj
            near_heights.append(area[ni][nj])
        if min(near_heights) < area[i][j]:
            pass
        elif min(near_heights) >= area[i][j]:
            area[i][j] = min(near_heights)

            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1

            queue = deque()
            queue.append((i, j))

            group_indexes = [(i, j)]
            possible = True
            now_height = area[i][j]

            while queue:
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or area[ny][nx] != now_height:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_indexes.append((ny, nx))

                next_queue = deque()
                next_height = 10_001
                for y, x in group_indexes:
                    if is_border(y, x):
                        possible = False
                        break
                    appended = False
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if area[ny][nx] != now_height:
                            next_height = min(next_height, area[ny][nx])
                            if not appended:
                                next_queue.append((y, x))
                                appended = True
                    if next_height < now_height:
                        possible = False
                        break

                if not possible:
                    break

                for gy, gx in group_indexes:
                    area[gy][gx] = next_height
                queue = next_queue
                now_height = next_height

answer = 0
for i in range(N):
    for j in range(M):
        answer += area[i][j] - origin_area[i][j]
print(answer)
