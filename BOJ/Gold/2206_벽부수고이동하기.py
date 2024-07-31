# 20240731
# 2:00:38

# (0, 0)에서 bfs로 닿는 거리 표시하고,
# (n - 1, m - 1)에서도 닪는 거리를 표시해 놓는다.
# 벽을 탐색하면서, "위에서 표시한 두 거리의 최소값(0은 안 닿는 것이므로 제외)의 합 +1(벽)"이 최단거리일 경우 갱신한다.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

n, m = map(int, input().split())
mp = [[int(i) for i in list(str(input()))] for _ in range(n)]


def oob(yy, xx):
    return not (0 <= yy < n) or not (0 <= xx < m)


# (0, 0) 에서 BFS 계산
queue = deque()
queue.append((0, 0))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

while queue:
    y, x = queue.popleft()
    distance = visited[y][x] + 1

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or visited[ny][nx] != 0 or mp[ny][nx] == 1:
            continue
        visited[ny][nx] = distance
        queue.append((ny, nx))

# (n - 1, m - 1) 에서 BFS 계산
q = deque()
q.append((n - 1, m - 1))

v = [[0] * m for _ in range(n)]
v[n - 1][m - 1] = 1

while q:
    y, x = q.popleft()
    distance = v[y][x] + 1

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx) or v[ny][nx] != 0 or mp[ny][nx] == 1:
            continue
        v[ny][nx] = distance
        q.append((ny, nx))

# 벽 부수기 없이 안 닿는다면, 임의의 최대값 설정.
answer = n * m + 1 if visited[n - 1][m - 1] == 0 else visited[n - 1][m - 1]

# 벽을 탐색
for i in range(n):
    for j in range(m):
        if mp[i][j] == 1:  # 벽이라면
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if oob(ni, nj) or visited[ni][nj] == 0:  # (0, 0)에서 시작한 거리에서 벽 상하좌우에 유효한 값이 없는 경우
                    continue

                reverse_min = n * m
                for ddi, ddj in direction:  # (n - 1, m - 1)에서 시작한 거리에서 유효한 최소값을 reverse_min으로 저장.
                    if di == ddi and dj == ddj:
                        continue
                    ri, rj = i + ddi, j + ddj
                    if oob(ri, rj) or v[ri][rj] == 0:
                        continue
                    reverse_min = min(reverse_min, v[ri][rj])

                if reverse_min == n * m:
                    continue
                else:
                    answer = min(answer, visited[ni][nj] + reverse_min + 1)  # 벽 상하좌우의 두 거리 각각의 유효한 값이 있다면 갱신

print(-1 if answer == n * m + 1 else answer)


# 내 풀이방식 말고 대중적인 방식은,
# queue에 담을 때 이전에 벽을 부쉈는지 여부도 담아서 BFS 하는 것.
# 벽 부쉈는지 여부에 따른 visited를 2개의 인덱스로 세팅했다는 것이 포인트!
"""
from collections import deque

n, m = map(int, input().split())
mp = [[int(i) for i in list(str(input()))] for _ in range(n)]

visited = [[[0] * m for _ in range(n)] for _ in range(2)]  # 0 : ? / 1 : 뚫은 벽 다시 뚫지 않게 뚫은 벽 표시
visited[0][0][0] = 1

queue = deque()
queue.append((0, 0, False, 1))  # y, x, 벽 부쉈는지 여부, distance


def oob(yy, xx):
    return not(0 <= yy < n) or not(0 <= xx < m)


direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = -1
while queue:
    y, x, break_wall, distance = queue.popleft()

    if y == n - 1 and x == m - 1:
        answer = distance
        break

    distance += 1
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        if not break_wall and not visited[0][ny][nx] and mp[ny][nx] == 1 and not visited[1][ny][nx]:  # 벽 안 부쉈고, 다음이 안부순 벽일때
            visited[1][ny][nx] = 1
            queue.append((ny, nx, True, distance))
        elif not break_wall and not visited[0][ny][nx] and mp[ny][nx] == 0:  # 벽 안 부쉈고, 다음이 빈땅일때
            visited[0][ny][nx] = 1
            queue.append((ny, nx, False, distance))
        elif break_wall and not visited[1][ny][nx] and mp[ny][nx] == 0:  # 벽 부쉈고, 다음이 빈땅일때
            visited[1][ny][nx] = 1
            queue.append((ny, nx, True, distance))

print(answer)
"""