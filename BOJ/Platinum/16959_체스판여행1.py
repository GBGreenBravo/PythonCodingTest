# 20241129
# 1 / 11

"""
0 0 0 1
0 0 0 0
0 0 0 0
0 2 0 0

초기상태가 비숍인 상태에서 1에서 2로 갈 때,
룩으로 바꿔서 3번만에 갈 수도 있지만
비숍으로 1칸 가고 나이트로 바꿔서 3번만에 갈 수 있는 경우를 생각하지 못했음.
"""


from collections import deque

knight_direction = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
bishop_direction = ((1, 1), (-1, 1), (1, -1), (-1, -1))
rook_direction = ((1, 0), (-1, 0), (0, 1), (0, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or N <= x


def make_connected():
    for sy in range(N):
        for sx in range(N):
            for dy, dx in knight_direction:
                ny, nx = sy + dy, sx + dx
                if not oob(ny, nx):
                    connected[sy][sx][0].append((ny, nx))
            for dy, dx in bishop_direction:
                ny, nx = sy + dy, sx + dx
                while not oob(ny, nx):
                    connected[sy][sx][1].append((ny, nx))
                    ny, nx = ny + dy, nx + dx
            for dy, dx in rook_direction:
                ny, nx = sy + dy, sx + dx
                while not oob(ny, nx):
                    connected[sy][sx][2].append((ny, nx))
                    ny, nx = ny + dy, nx + dx


def bfs(sy, sx):
    min_visited[1] = 0

    visited = [[[[N**2 * 2] * 3 for _ in range(N**2 + 1)] for _ in range(N)] for _ in range(N)]
    visited[sy][sx][1][0] = 0
    visited[sy][sx][1][1] = 0
    visited[sy][sx][1][2] = 0

    queue = deque()
    queue.append((sy, sx, 1, 0, 0))
    queue.append((sy, sx, 1, 1, 0))
    queue.append((sy, sx, 1, 2, 0))

    while queue:
        y, x, now, who, distance = queue.popleft()

        if who == 2 and min_visited[now] + 2 < distance:
            continue
        if who in (0, 2) and min_visited[now] + 3 < distance:
            continue

        if now == N**2:
            continue

        if who == 0:  # knight
            distance_arr = [distance + 1, distance + 2, distance + 2]
        elif who == 1:  # bishop
            distance_arr = [distance + 2, distance + 1, distance + 2]
        else:  # rook
            distance_arr = [distance + 2, distance + 2, distance + 1]

        for next_who in range(3):
            next_dist = distance_arr[next_who]
            for ny, nx in connected[y][x][next_who]:
                if area[ny][nx] == now + 1:
                    if next_dist < visited[ny][nx][now + 1][next_who]:
                        min_visited[now + 1] = min(min_visited[now + 1], next_dist)
                        visited[ny][nx][now + 1][next_who] = next_dist
                        queue.append((ny, nx, now + 1, next_who, next_dist))

                elif next_dist < visited[ny][nx][now][next_who]:
                    visited[ny][nx][now][next_who] = next_dist
                    queue.append((ny, nx, now, next_who, next_dist))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

connected = [[[[] for _ in range(3)] for _ in range(N)] for _ in range(N)]
make_connected()

min_visited = [N**2 * 2] * (N**2 + 1)
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            bfs(i, j)
print(min_visited[-1])
