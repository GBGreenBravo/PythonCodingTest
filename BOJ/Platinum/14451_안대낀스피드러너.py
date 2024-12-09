# 20241209
# 47:44
# 1 / 2

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def cal_distance(sy, sx, sd):
    v = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    v[sy][sx][sd] = 1
    q = deque()
    q.append((sy, sx, sd, 1))
    while q:
        y, x, d, distance = q.popleft()
        if (y, x) == (N - 1, N - 1):
            return distance - 1

        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        if not oob(ny, nx) and not area[ny][nx] and not v[ny][nx][d]:
            v[ny][nx][d] = distance + 1
            q.append((ny, nx, d, distance + 1))

        if not v[y][x][(d + 1) % 4]:
            v[y][x][(d + 1) % 4] = distance + 1
            q.append((y, x, (d + 1) % 4, distance + 1))

        if not v[y][x][(d - 1) % 4]:
            v[y][x][(d - 1) % 4] = distance + 1
            q.append((y, x, (d - 1) % 4, distance + 1))


N = int(input())
area = [[int(i == 'H') for i in str(input())] for _ in range(N)]
area.reverse()
visited = [[[[[[1e4 for _ in range(4)] for _ in range(N)] for _ in range(N)] for _ in range(4)] for _ in range(N)] for _ in range(N)]
visited[0][0][1][0][0][0] = 0
queue = deque()
queue.append((0, 0, 1, 0, 0, 0, 0))
answer = 1e4
while queue:
    y1, x1, d1, y2, x2, d2, route_cnt = queue.popleft()

    # 직진
    dy1, dx1 = direction[d1]
    ny1, nx1 = y1 + dy1, x1 + dx1
    if oob(ny1, nx1) or area[ny1][nx1]:
        ny1, nx1 = y1, x1
    dy2, dx2 = direction[d2]
    ny2, nx2 = y2 + dy2, x2 + dx2
    if oob(ny2, nx2) or area[ny2][nx2]:
        ny2, nx2 = y2, x2

    if (ny1, nx1) == (N - 1, N - 1):
        answer = min(answer, route_cnt + 1 + cal_distance(ny2, nx2, d2))
        continue
    elif (ny2, nx2) == (N - 1, N - 1):
        answer = min(answer, route_cnt + 1 + cal_distance(ny1, nx1, d1))
        continue
    elif visited[ny1][nx1][d1][ny2][nx2][d2] > route_cnt + 1:
        visited[ny1][nx1][d1][ny2][nx2][d2] = route_cnt + 1
        queue.append((ny1, nx1, d1, ny2, nx2, d2, route_cnt + 1))

    # 우회전
    nd1 = (d1 + 1) % 4
    nd2 = (d2 + 1) % 4
    if visited[y1][x1][nd1][y2][x2][nd2] > route_cnt + 1:
        visited[y1][x1][nd1][y2][x2][nd2] = route_cnt + 1
        queue.append((y1, x1, nd1, y2, x2, nd2, route_cnt + 1))

    # 좌회전
    nd1 = (d1 - 1) % 4
    nd2 = (d2 - 1) % 4
    if visited[y1][x1][nd1][y2][x2][nd2] > route_cnt + 1:
        visited[y1][x1][nd1][y2][x2][nd2] = route_cnt + 1
        queue.append((y1, x1, nd1, y2, x2, nd2, route_cnt + 1))

print(answer)
