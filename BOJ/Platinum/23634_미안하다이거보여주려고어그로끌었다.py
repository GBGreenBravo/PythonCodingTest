# 20241209
# 1:00:37
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def init_bfs(sy, sx):
    visited[sy][sx] = group_flag
    queue = deque()
    queue.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 2:
                continue
            visited[ny][nx] = group_flag
            queue.append((ny, nx))


def find(group_idx, x):
    if parents[group_idx][x] != x:
        parents[group_idx][x] = find(group_idx, parents[group_idx][x])
    return parents[group_idx][x]


def union(group_idx, a, b):
    global remain_cnt
    if a < b:
        parents[group_idx][b] = a
    else:
        parents[group_idx][a] = b
    remain_cnt -= 1


def merge_fires_when_start():
    for y, x, now in start_queue:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] != 0:
                continue
            f = find(visited[y][x], nows[ny][nx])
            nf = find(visited[y][x], now)
            if f != nf:
                union(visited[y][x], f, nf)
                nows[ny][nx] = now


def spreading_bfs(queue):
    time, fire = 0, len(queue)
    while remain_cnt and queue:
        time += 1
        next_queue = []
        for y, x, now in queue:
            now_group = visited[y][x]
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area[ny][nx] in (0, 2):
                    continue
                fire += 1
                area[ny][nx] = 0
                nows[ny][nx] = now
                next_queue.append((ny, nx, now))
                for ddy, ddx in direction:
                    nny, nnx = ny + ddy, nx + ddx
                    if oob(nny, nnx) or area[nny][nnx] != 0:
                        continue
                    f = find(now_group, now)
                    nf = find(now_group, nows[nny][nnx])
                    if f != nf:
                        union(now_group, f, nf)
        queue = next_queue
    print(time, fire)


N, M = map(int, input().split())
area = [[int(i) for i in str(input())] for _ in range(N)]

visited = [[0] * M for _ in range(N)]
nows = [[0] * M for _ in range(N)]
start_queue = []
parents = [None]
group_flag = 0
for i in range(N):
    for j in range(M):
        if not area[i][j] and not visited[i][j]:
            group_flag += 1
            init_bfs(i, j)
        if not area[i][j]:
            if visited[i][j] + 1 > len(parents):
                parents.append([0, 1])
                p = 1
            else:
                p = parents[visited[i][j]][-1] + 1
                parents[visited[i][j]].append(p)
            start_queue.append((i, j, p))
            nows[i][j] = p

remain_cnt = 0
for i in range(1, len(parents)):
    for j in range(2, len(parents[i])):
        remain_cnt += 1
merge_fires_when_start()

spreading_bfs(start_queue)
