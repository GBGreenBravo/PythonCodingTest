# 20241224
# 38:34
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def grouping():
    flag = 0
    visited = [[0] * M for _ in range(N)]
    for ssy in range(N):
        for ssx in range(M):
            if area[ssy][ssx] == '.' and not visited[ssy][ssx]:
                flag += 1
                visited[ssy][ssx] = flag
                queue = deque([(ssy, ssx)])
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or area[ny][nx] != '.':
                            continue
                        visited[ny][nx] = flag
                        queue.append((ny, nx))
    return visited, flag


def connecting():
    graph = [None] + [set() for _ in range(group_cnt)]
    for d_idx, (dy, dx) in enumerate(direction):
        if d_idx <= 1:
            for y in range(N):
                x = 0 if d_idx == 0 else M - 1
                in_a_row = None
                while 0 <= x < M:
                    if area[y][x]:
                        if not in_a_row:
                            in_a_row = [area[y][x], 0]
                        else:
                            in_a_row[1] += 1
                    else:
                        if not in_a_row:
                            pass
                        else:
                            now = in_a_row[0]
                            moved = in_a_row[1]
                            for dist in range(1, moved + 1):
                                ny, nx = y, x + dx * dist
                                if nx < 0 or M <= nx:
                                    break
                                elif area[ny][nx]:
                                    graph[now].add(area[ny][nx])
                        in_a_row = None

                    y, x = y, x + dx
        else:
            for x in range(M):
                y = 0 if d_idx == 2 else N - 1
                in_a_row = None
                while 0 <= y < N:
                    if area[y][x]:
                        if not in_a_row:
                            in_a_row = [area[y][x], 0]
                        else:
                            in_a_row[1] += 1
                    else:
                        if not in_a_row:
                            pass
                        else:
                            now = in_a_row[0]
                            moved = in_a_row[1]
                            for dist in range(1, moved + 1):
                                ny, nx = y + dy * dist, x
                                if ny < 0 or N <= ny:
                                    break
                                elif area[ny][nx]:
                                    graph[now].add(area[ny][nx])
                        in_a_row = None

                    y, x = y + dy, x

    return graph


def bfs():
    visited = [None] + [0] * group_cnt
    visited[area[sy][sx]] = 1
    queue = deque([area[sy][sx]])
    while queue and not visited[area[ey][ex]]:
        now = queue.popleft()
        for nex in connected[now]:
            if not visited[nex]:
                visited[nex] = 1
                queue.append(nex)
    return visited[area[ey][ex]]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    area = [list(str(input())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if area[i][j] == 'S':
                sy, sx = i, j
                area[i][j] = '.'
            elif area[i][j] == 'E':
                ey, ex = i, j
                area[i][j] = '.'
    area, group_cnt = grouping()
    connected = connecting()
    print("YES" if bfs() else "NO")
