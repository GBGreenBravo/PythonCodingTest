# 20241010
# 25:26
# 1 / 2

# area[ey][ex]를 2로 변경했던 것 까먹어서, 디버깅에 시간 소요됨.
# 탈출 못할 때 -1 출력 까먹어서 한번 틀림.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or m <= xx


n, m = map(int, input().split())
sy, sx = map(lambda inp: int(inp) - 1, input().split())
ey, ex = map(lambda inp: int(inp) - 1, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0] * m for _ in range(n)] for _ in range(2)]
visited[0][sy][sx] = 1

queue = deque()
queue.append((0, sy, sx))

while queue:
    magic_used, y, x = queue.popleft()
    distance = visited[magic_used][y][x]

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if not magic_used:
            if visited[0][ny][nx]:
                continue
            if not area[ny][nx]:
                visited[0][ny][nx] = distance + 1
                queue.append((0, ny, nx))
            elif not visited[1][ny][nx] or visited[1][ny][nx] > distance + 1:
                visited[1][ny][nx] = distance + 1
                queue.append((1, ny, nx))
        else:
            if visited[1][ny][nx] and visited[1][ny][nx] <= distance + 1:
                continue
            if area[ny][nx]:
                continue
            elif not area[ny][nx]:
                visited[1][ny][nx] = distance + 1
                queue.append((1, ny, nx))

answer = n * m
if visited[0][ey][ex]:
    answer = min(answer, visited[0][ey][ex] - 1)
if visited[1][ey][ex]:
    answer = min(answer, visited[1][ey][ex] - 1)
print(answer if answer != n * m else -1)
