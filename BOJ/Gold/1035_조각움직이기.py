# 20241023
# 26:20
# 1 / 1

# 각 조각별 좌표별 BFS최단거리 저장한 배열들을 distances에 저장하고, (다른 조각들이 BFS동선에 걸리는 경우보다 더 효율적인 최소값이 존재함.)
# 25 * 24 * 23 * 22 * 21 (5*5에서 겹치지 않게 5개 뽑는 경우의 수)의 순열에 대해서, 서로 연결되는지 판단하고 최소값 갱신해주면 됨.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 5 <= y or x < 0 or 5 <= x


def bfs(sy, sx):
    visited = [[0] * 5 for _ in range(5)]
    visited[sy][sx] = 1

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx]:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))

    for y in range(5):
        for x in range(5):
            visited[y][x] -= 1
    return visited


def check():
    if len(dfs_arr) <= 1:
        return True

    check_visited = [[0] * 5 for _ in range(5)]
    for sy, sx in dfs_arr[1:]:
        check_visited[sy][sx] = 1

    queue = deque()
    queue.append(dfs_arr[0])

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or not check_visited[ny][nx]:
                continue
            check_visited[ny][nx] = 0
            queue.append((ny, nx))

    return not sum(map(sum, check_visited))


def dfs(cnt, now_answer):
    global min_answer

    if now_answer >= min_answer:
        return

    if cnt == len_pieces:
        if check():
            min_answer = min(min_answer, now_answer)
        return

    for y in range(5):
        for x in range(5):
            if (y, x) not in dfs_arr:
                dfs_arr.append((y, x))
                dfs(cnt + 1, now_answer + distances[cnt][y][x])
                dfs_arr.pop()


area = [[int(inp == '*') for inp in str(input())] for _ in range(5)]

distances = []
for i in range(5):
    for j in range(5):
        if area[i][j]:
            distances.append(bfs(i, j))
len_pieces = len(distances)

min_answer = 25 * 5
dfs_arr = []
dfs(0, 0)
print(min_answer)
