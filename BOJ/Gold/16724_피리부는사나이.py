# 20240818
# 15:37
# 1 / 1

from collections import deque

direction = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}


def bfs(sy, sx):
    visited[sy][sx] = True

    queue = deque()
    queue.append((sy, sx))

    now_cycle = {(sy, sx)}  # 현재 bfs()에서 탐색되는 모든 좌표 저장
    cycle_here = False

    while queue:
        y, x = queue.popleft()
        dy, dx = direction[area[y][x]]
        ny, nx = y + dy, x + dx

        if (ny, nx) in now_cycle:  # 만약 다음좌표가 이 함수에서 탐색했던 좌표면, cycle 구성한다는 뜻
            cycle_here = True

        if not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((ny, nx))
            now_cycle.add((ny, nx))

    if cycle_here:  # cycle 구성하면 cnt += 1
        global cycle_cnt
        cycle_cnt += 1

n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
cycle_cnt = 0  # 정답이 될 cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # not visited에서 다 카운트해주면, 기존 사이클에 포함되는 not visited도 존재하기에 (RRLL과 같은 경우)
            bfs(i, j)  # cycle 구성되는 bfs()에서만 카운트해야 함.

print(cycle_cnt)
