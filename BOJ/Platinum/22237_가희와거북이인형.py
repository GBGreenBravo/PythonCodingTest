# 20241021
# 59:52
# 1 / 6

# 거북이좌표가 엄청 많을 수도 있는데, 이를 고려하지 못하고 처음에는
# 이동하는 좌표별 다른 거북이 좌표들을 다 계산해서 2번 시간초과.
# (장애물 최대 20개이기에, 장애물 기준으로 기준좌표가 못 가는 좌표들 미리 계산해둠. -> set_obstacles() 함수로 반영)

# 거북이가 구성된 turtles 배열의 첫 값을 (0, 0)으로 고정시켜두고,
# BFS로 찾는 좌표들들은 기준 좌표로부터의 (tdi, tdj)로 저장했음.
# 이렇게 일반적인 좌표가 아닌 기준점으로부터의 거리였기에 헷갈렸고, oob_first()의 경계를 제대로 설정하지 못해 3번 틀림.

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
direction_dict = {(0, 1): "R", (0, -1): "L", (1, 0): "D", (-1, 0): "U"}


def oob(y, x):
    return y < 0 or R <= y or x < 0 or C <= x


def oob_first(y, x):
    return y < 0 or R - bottom <= y or x < -left or C - right <= x


def set_obstacles():
    for oy, ox in obstacles:
        for ty, tx in turtles:
            ony, onx = oy - ty, ox - tx
            if not oob(ony, onx):
                visited[ony][onx] = -1


def find_home_ables():
    found = set()
    for ty, tx in turtles:
        ohy, ohx = home[0] - ty, home[1] - tx
        if not oob(ohy, ohx):
            found.add((ohy, ohx))
    return found


def bfs():
    while queue:
        y, x, route = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob_first(ny, nx) or visited[ny][nx]:
                continue
            if (ny, nx) in home_ables:
                return route + direction_dict[(dy, dx)]
            visited[ny][nx] = 1
            queue.append((ny, nx, route + direction_dict[(dy, dx)]))
    return None


R, C = map(int, input().split())
area = [list(str(input())) for _ in range(R)]

home, turtles, obstacles = None, None, []
for i in range(R):
    for j in range(C):
        if area[i][j] == 'H':
            home = (i, j)
        elif not turtles and area[i][j] == 'T':
            si, sj = i, j
            turtles = [(0, 0)]

            t_visited = [[0] * C for _ in range(R)]
            t_visited[si][sj] = 1
            t_queue = deque([(i, j)])

            while t_queue:
                ci, cj = t_queue.popleft()
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if oob(ni, nj) or area[ni][nj] != 'T' or t_visited[ni][nj]:
                        continue
                    turtles.append((ni - i, nj - j))
                    t_visited[ni][nj] = 1
                    t_queue.append((ni, nj))
        elif area[i][j] == '#':
            obstacles.append((i, j))
bottom, left, right = -1, R, -1
for ti, tj in turtles:
    bottom = max(bottom, ti)
    left = min(left, tj)
    right = max(right, tj)

visited = [[0] * C for _ in range(R)]
visited[si][sj] = 1

set_obstacles()
home_ables = find_home_ables()

queue = deque()
queue.append((si, sj, ''))
result = bfs()
print(result if result else -1)
