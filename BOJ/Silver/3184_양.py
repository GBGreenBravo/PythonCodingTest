# 20240818
# 14:00
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def bfs(sy, sx):
    visited[sy][sx] = True

    queue = deque()
    queue.append((sy, sx))

    sheep_cnt, wolves_cnt = 0, 0

    while queue:
        y, x = queue.popleft()

        if area[y][x] == 'o':  # 현재위치에 양 있으면
            sheep_cnt += 1
        elif area[y][x] == 'v':  # 현재위치에 늑대 있으면
            wolves_cnt += 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):  # 하나라도 울타리 없이 영역 밖을 접한다면, 영역으로 간주되지 않음
                return
            if area[ny][nx] == '#' or visited[ny][nx]:  # 울타리거나 이미 방문했던 곳이라면, continue
                continue
            visited[ny][nx] = True
            queue.append((ny, nx))

    global final_sheep_cnt, final_wolves_cnt
    # 현재 bfs에서 지나온 영역의 총 양/늑대 수를 비교하고, 반영
    if sheep_cnt > wolves_cnt:
        final_sheep_cnt += sheep_cnt
    else:
        final_wolves_cnt += wolves_cnt


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

final_sheep_cnt, final_wolves_cnt = 0, 0
for i in range(n):
    for j in range(m):
        if area[i][j] != '#' and not visited[i][j]:
            bfs(i, j)

print(final_sheep_cnt, final_wolves_cnt)
