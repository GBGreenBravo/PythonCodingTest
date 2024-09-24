# 20240924
# 38:53
# 1 / 4

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or h <= y or x < 0 or w <= x


def bfs(sy, sx):
    global go_on, documents

    if visited[sy][sx]:  # 이전의 BFS에서 탐색된 시작점 -> return
        return
    elif area[sy][sx] == '.':  # 빈칸 -> 탐색
        pass
    elif area[sy][sx] in list('abcdefghijklmnopqrstuvwxyz'):  # 열쇠 -> 줍기 & 탐색
        keys.append(area[sy][sx])
        area[sy][sx] = '.'
        go_on = True
    elif area[sy][sx] == '$':  # 문서 -> 줍기 & 탐색
        area[sy][sx] = '.'
        documents += 1
    elif area[sy][sx] in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') and chr(ord(area[sy][sx]) + 32) in keys:  # 열 수 있는 문 -> 열기 & 탐색
        area[sy][sx] = '.'
        go_on = True
    elif area[sy][sx] in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):  # 못 여는 문 -> return
        return

    # (BFS) 시작점과 인접한 칸들 탐색 시작
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == '*':  # 영역 밖 / 이미 방문 / 벽 -> continue
                continue

            if area[ny][nx] in list('abcdefghijklmnopqrstuvwxyz'):  # 열쇠 -> 줍기
                keys.append(area[ny][nx])
                area[ny][nx] = '.'
                go_on = True
            elif area[ny][nx] == '$':  # 문서 -> 줍기
                area[ny][nx] = '.'
                documents += 1
            elif area[ny][nx] in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') and chr(ord(area[ny][nx]) + 32) in keys:  # 열 수 있는 문 -> 열기
                area[ny][nx] = '.'
                go_on = True
            elif area[ny][nx] in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):  # 못 여는 문 -> continue
                continue

            visited[ny][nx] = 1
            queue.append((ny, nx))


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    area = [list(str(input())) for _ in range(h)]

    # 처음부터 갖는 열쇠 배열
    keys = list(str(input()))
    if keys == ['0']:
        keys = []

    # 줍는 문서 수
    documents = 0

    # 탐색 가능한 시작점들
    start_points = []
    for i in range(h):
        if area[i][0] != '*':
            start_points.append((i, 0))
        if area[i][w - 1] != '*':
            start_points.append((i, w - 1))
    for i in range(1, w):
        if area[0][i] != '*':
            start_points.append((0, i))
        if area[h - 1][i] != '*':
            start_points.append((h - 1, i))

    # 열쇠 찾거나 새로운 문 열면 go_on Flag로 반복해야 함.
    go_on = True
    while go_on:
        go_on = False

        # 새로운 열쇠가 추가되거나, 새로운 문이 열렸으므로, visited도 초기화
        visited = [[0] * w for _ in range(h)]

        # 벽이 아닌 시작점부터 시작
        for spy, spx in start_points:
            bfs(spy, spx)

    print(documents)
