# 20241001
# 13:48
# 1 / 1

# 17142_연구소3

"""
풀이 시간: 14분 (16:11 - 16:25)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:11 - 16:15)


2. 구현 (16:15 - 16:22)


3. 디버깅 (16:22 - 16:24)
    처음 입력 시, 바이러스가 아예 없는 경우에 0을 출력해야 하는데 -1을 출력하는 이슈가 있었고, 그에 따른 로직을 추가했습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def check():
    visited = [[0] * n for _ in range(n)]
    queue = deque()

    for dfs_idx in dfs_arr:
        sy, sx = candidates[dfs_idx]
        visited[sy][sx] = 1
        queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 1:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))

    max_distance = 0
    for y in range(n):
        for x in range(n):
            if area[y][x] == 0:
                if not visited[y][x]:
                    return
                max_distance = max(max_distance, visited[y][x])

    global min_answer
    min_answer = min(min_answer, max_distance - 1)


def dfs(cnt, start_idx):
    if not min_answer:
        return

    if cnt == m:
        check()
        return

    for idx in range(start_idx, len_candidates):
        dfs_arr.append(idx)
        dfs(cnt + 1, idx + 1)
        dfs_arr.pop()


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

if not sum(map(lambda rr: rr.count(0), area)):
    print(0)
else:
    candidates = []
    for i in range(n):
        for j in range(n):
            if area[i][j] == 2:
                candidates.append((i, j))
    len_candidates = len(candidates)

    min_answer = n * n
    dfs_arr = []
    dfs(0, 0)
    print(-1 if min_answer == n * n else min_answer)
