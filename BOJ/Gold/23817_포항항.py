# 20241109
# 26:06
# 1 / 1

"""
무작정 BFS 하면 시간초과날 것이 보였음.
그래서 "시작점과 가게들 & 가게들 간"의 거리를 미리 BFS로 각각 구해주고,
해당 거리들을 바탕으로 DFS를 하면 되겠다고 생각함.

가게 수가 최대 20개이므로, 시작점까지 포함하면 21개의 노드
이 노드들 다 연결해주는 시간복잡도: N * M * comb(21, 2) = 10**3 * 10**3 * 210
위 정보들을 토대로 시작점에서 시작하는 DFS 시간복잡도: perm(20, 5) = 1_860_480
구상 시간복잡도: 10**3 * 10**3 * 210 + 1_860_480
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]

points = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 'S':
            points.insert(0, (i, j))
        elif area[i][j] == 'K':
            points.append((i, j))

len_points = len(points)
connected = [[0] * len_points for _ in range(len_points)]
for i in range(len_points):
    si, sj = points[i]

    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1

    queue = deque()
    queue.append((si, sj))

    while queue:
        ci, cj = queue.popleft()
        distance = visited[ci][cj]

        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            if oob(ni, nj) or visited[ni][nj] or area[ni][nj] == 'X':
                continue
            if area[ni][nj] in ('S', 'K'):
                j = points.index((ni, nj))
                connected[i][j] = distance
                connected[j][i] = distance
            visited[ni][nj] = distance + 1
            queue.append((ni, nj))


def dfs(cnt, now_answer):
    global min_answer

    if now_answer >= min_answer:
        return

    if cnt == 5:
        min_answer = now_answer
        return

    for idx in range(len(points)):
        if connected[dfs_arr[-1]][idx] and idx not in dfs_arr:
            dfs_arr.append(idx)
            dfs(cnt + 1, now_answer + connected[dfs_arr[-2]][idx])
            dfs_arr.pop()


min_answer = N * M * 5
dfs_arr = [0]
dfs(0, 0)
print(min_answer if min_answer != N * M * 5 else -1)
