# 20240818
# 39:43
# 1 / 6

# DP 없이 DFS/BFS로만 각각 구현했을 때 시간초과가 났는데, 그 시간복잡도를 계산하지 못해 계속 틀렸던 문제.

from heapq import heappop, heappush

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))


def oob(y, x):
    return y < 0 or m <= y or x < 0 or n <= x


def bfs():
    visited = [[0] * n for _ in range(m)]  # 현재 좌표까지의 루트의 누적합을 저장할 배열
    visited[0][0] = 1

    queue = []
    if n > 1 and area[0][1] < area[0][0]:  # indexError 방지를 위한 처리
        heappush(queue, (-area[0][1], 0, 1))
    if m > 1 and area[1][0] < area[0][0]:
        heappush(queue, (-area[1][0], 1, 0))

    while queue:
        _, y, x = heappop(queue)
        area_yx = area[y][x]

        if visited[y][x]:  # 이미 방문했던 곳이라면 continue
            continue

        tmp = 0
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] <= area_yx:  # 현재보다 큰 곳은 이미 방문했던 곳
                continue
            tmp += visited[ny][nx]  # 카운트된 경로 더하기
        visited[y][x] = tmp

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] >= area_yx:  # 현재보다 작은 곳은 나중에 가야할 곳
                continue

            heappush(queue, (-area[ny][nx], ny, nx))  # 값이 높은 순대로 조회해야 하므로, - 붙이기

    return visited[-1][-1]


m, n = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(m)]

print(bfs())


# 상하좌우 for문 2번을 1번으로 병합.
"""
# 20240818
# 39:43
# 1 / 6

# DP 없이 DFS/BFS로만 각각 구현했을 때 시간초과가 났는데, 그 시간복잡도를 계산하지 못해 계속 틀렸던 문제.

from heapq import heappop, heappush

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))


def oob(y, x):
    return y < 0 or m <= y or x < 0 or n <= x


def bfs():
    visited = [[0] * n for _ in range(m)]  # 현재 좌표까지의 루트의 누적합을 저장할 배열
    visited[0][0] = 1

    queue = []
    if n > 1 and area[0][1] < area[0][0]:  # indexError 방지를 위한 처리
        heappush(queue, (-area[0][1], 0, 1))
    if m > 1 and area[1][0] < area[0][0]:
        heappush(queue, (-area[1][0], 1, 0))

    while queue:
        area_yx, y, x = heappop(queue)
        area_yx = -area_yx

        if visited[y][x]:  # 이미 방문했던 곳이라면 continue
            continue

        tmp = 0

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] == area_yx:
                continue

            if area[ny][nx] > area_yx:  # 현재보다 큰 곳은 이미 방문했던 곳
                tmp += visited[ny][nx]  # 카운트된 경로 더하기
            elif area[ny][nx] < area_yx:  # 현재보다 작은 곳은 나중에 가야할 곳
                heappush(queue, (-area[ny][nx], ny, nx))  # 값이 높은 순대로 조회해야 하므로, - 붙이기

        visited[y][x] = tmp

    return visited[-1][-1]


m, n = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(m)]

print(bfs())
"""