# 20241130
# 44:26
# 1 / 1

from collections import deque

direction_4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_8 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or N <= y or x < 0 or M <= x


def carve(sy, sx):
    if not area_visited[sy][sx] and area[sy][sx] == '.':
        area_visited[sy][sx] = 1
        queue = deque([(sy, sx)])
        while queue:
            y, x = queue.popleft()
            for dy, dx in direction_4:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or area_visited[ny][nx] or area[ny][nx] != '.':
                    continue
                area_visited[ny][nx] = 1
                queue.append((ny, nx))


def init_visit():
    for sx in range(M):
        carve(0, sx)
        carve(N - 1, sx)
    for sy in range(N):
        carve(sy, 0)
        carve(sy, M - 1)


def fill_and_find_others(sy, sx):
    other = []  # 안에서 다른 섬 좌표 발견되면 여기 추가

    area_visited[sy][sx] = 1
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction_4:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area_visited[ny][nx]:
                continue
            if area[ny][nx] != '.':
                other.append((ny, nx))
                continue
            area_visited[ny][nx] = 1
            queue.append((ny, nx))

    # 다른 섬 발견되면, 해당 섬 높이 구해서 추가
    other_heights = []
    for oy, ox in other:
        if not area_visited[oy][ox]:
            other_heights.append(cal_height(oy, ox))

    return other_heights  # 안의 섬들 높이 반환


# 현재 좌표의 섬 높이 계산해서, 저장 & 반환
def cal_height(sy, sx):
    area_visited[sy][sx] = 1
    queue = deque([(sy, sx)])

    # 안에 . 있으면 해당 좌표 기반으로 탐색 필요
    inner = []

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction_8:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area_visited[ny][nx]:
                continue
            if area[ny][nx] != 'x':
                inner.append((ny, nx))
                continue
            area_visited[ny][nx] = 1
            queue.append((ny, nx))

    # 안에 섬 있으면, 그 섬들의 높이 담을 배열
    found_heights = []
    for iy, ix in inner:  # 안에 . 있다면 .을 먼저 방문처리 다 하고, 찾은 섬들 높이 배열 추가
        if not area_visited[iy][ix]:
            found_heights.extend(fill_and_find_others(iy, ix))

    # 안에 다른 섬 없으면, 현재 함수의 섬 높이 = 0
    if not found_heights:
        heights[0] = heights.get(0, 0) + 1
        return 0

    # 안에 섬 있으면, 그 섬들 높이 최대값 + 1
    now_height = max(found_heights) + 1
    heights[now_height] = heights.get(now_height, 0) + 1
    return now_height


N, M = map(int, input().split())
area = [list(str(input())) for _ in range(N)]

area_visited = [[0] * M for _ in range(N)]
init_visit()  # 테두리에서 . 찾아서 BFS로 . 방문처리

heights = dict()
for i in range(N):
    for j in range(M):
        if not area_visited[i][j]:
            height = cal_height(i, j)

if not heights:
    print(-1)
else:
    print(*[v for h, v in sorted(heights.items())])
