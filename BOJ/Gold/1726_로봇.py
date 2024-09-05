# 20240905
# 1 / 1

from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북


def oob(yy, xx):
    return yy < 0 or m <= yy or xx < 0 or n <= xx


m, n = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(m)]

# 입력받는 방향을, 회전하기 편하게 direction의 index로 변경
input_direction = {1: 0, 2: 2, 3: 1, 4: 3}

# 출발지/도착지의 좌표와 방향 조정
sy, sx, sd = map(int, input().split())
ey, ex, ed = map(int, input().split())
sy, sx, ey, ex = sy - 1, sx - 1, ey - 1, ex - 1
sd = input_direction[sd]
ed = input_direction[ed]

visited = [[[0] * 4 for _ in range(n)] for _ in range(m)]
visited[sy][sx][sd] = 1

queue = deque()
queue.append((sy, sx, sd))

# BFS
while queue:
    y, x, d = queue.popleft()
    commands = visited[y][x][d]  # (여기까지 쓰인 명령 수 + 1)의 값

    if y == ey and x == ex and d == ed:  # 도착지면 종료
        break

    # 명령 2
    for di in [(d + 1) % 4, d - 1]:  # 우회전/좌회전
        if not visited[y][x][di]:
            visited[y][x][di] = commands + 1
            queue.append((y, x, di))

    # 명령 1
    dy, dx = direction[d]
    for dd in range(1, 4):  # 1~3의 거리
        ny, nx = y + dy * dd, x + dx * dd
        if oob(ny, nx) or area[ny][nx]:  # 영역 밖이거나 막혀있으면 break
            break
        if visited[ny][nx][d]:  # 이미 방문한 곳이면 continue
            continue
        visited[ny][nx][d] = commands + 1
        queue.append((ny, nx, d))

print(visited[ey][ex][ed] - 1)  # 도착지까지의 명령 개수 출력
