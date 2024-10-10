# 20241010
# 17:37
# 1 / 2

# 최대값 설정이 잘못 됐음.
# n*n으로 했을 때의 반례: 2*2배열에서 주기 5의 다리를 놓는 경우

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def bfs():
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()
        distance = visited[y][x]

        if area[y][x] != 1 and (distance - 1) % area[y][x]:
            visited[y][x] += 1
            queue.append((y, x))
            continue

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or not area[ny][nx]:
                continue
            if area[y][x] != 1 and area[ny][nx] != 1:
                continue
            visited[ny][nx] = distance + 1
            queue.append((ny, nx))

            if ny == n - 1 and nx == n - 1:
                return distance


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

answer = n * n * m

for i in range(n):
    for j in range(n):
        if not area[i][j]:
            near_cliff_cnt = 0
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if oob(ni, nj):
                    continue
                if not area[ni][nj]:
                    near_cliff_cnt += 1
            if near_cliff_cnt < 2:
                area[i][j] = m
                bfs_result = bfs()
                if bfs_result:
                    answer = min(answer, bfs())
                area[i][j] = 0

print(answer)
