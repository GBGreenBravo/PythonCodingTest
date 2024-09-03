# 20240903
# 13:48
# 1 / 2

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or h <= yy or xx < 0 or w <= xx


def escape():
    queue = deque()
    for fy, fx in fires:
        queue.append((fy, fx, True))  # 불 먼저 큐에 담기(불 붙을 칸 이동하면 안 되기에)
    queue.append((sy, sx, False))  # 상근이 좌표 넣어주기

    visited = [[0] * w for _ in range(h)]  # 상근이 방문체크 배열
    visited[sy][sx] = 1

    while queue:
        y, x, is_fire = queue.popleft()

        if is_fire:  # 불이라면
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] != '.':
                    continue
                area[ny][nx] = '*'  # 빈칸을 불로 만들기
                queue.append((ny, nx, True))

        else:  # 상근이라면
            distance = visited[y][x]

            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx):  # 영역 밖(탈출)이라면
                    return distance  # 이동거리 반환
                if not visited[ny][nx] and area[ny][nx] == '.':  # visited 체크 안 해줘서, 메모리 초과 났었음....
                    visited[ny][nx] = distance + 1
                    queue.append((ny, nx, False))

    return "IMPOSSIBLE"


tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    area = [list(str(input())) for _ in range(h)]

    fires = []
    for i in range(h):
        for j in range(w):
            if area[i][j] == '@':
                area[i][j] = '.'
                sy, sx = i, j
            elif area[i][j] == '*':
                fires.append((i, j))

    print(escape())
